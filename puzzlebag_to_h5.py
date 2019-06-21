from __future__ import print_function
import sys
import json
import rosbag
import h5py
import numpy as np

bag_filename = sys.argv[1]
print('converting {}'.format(bag_filename))

bag = rosbag.Bag(bag_filename)

for topic, msg, t in bag.read_messages(topics=['/puzzleboxes_param']):
    param = json.loads(msg.data)
    break # only need 1


index_to_attr = {}
index_to_data = {}
for i, protocol in enumerate(param['regions']['protocols']):
    if protocol['fly']:
        # Create attributes for each region
        attr_dict = {'index': i} 
        for k,v in protocol.items():
            attr_dict[k] = v
        attr_dict['center'] = param['regions']['centers'][i]
        attr_dict['param'] = param
        index_to_attr[i] = attr_dict

        # Create datasets for each region (initially empty)
        data_keys = ['elapsed_t', 'led_enabled', 'object_found','x', 'y','classifier','led'] 
        data_dict = {}
        for k in data_keys:
            data_dict[k] = []
        index_to_data[i] = data_dict
    

# Read messages and populate datasets
for msg_count, msg_item in enumerate(bag.read_messages(topics=['/puzzleboxes_data'])):
    topic, msg, t = msg_item
    for i, region_data in enumerate(msg.region_data_list):
        if i in index_to_data:
            index_to_data[i]['elapsed_t'].append(msg.elapsed_time)
            index_to_data[i]['led_enabled'].append(msg.led_enabled)
            index_to_data[i]['object_found'].append(region_data.object_found)
            index_to_data[i]['x'].append(region_data.x)
            index_to_data[i]['y'].append(region_data.y)
            index_to_data[i]['classifier'].append(region_data.classifier)
            index_to_data[i]['led'].append(region_data.led)

# Save data to hdf5 file
for i, attr_dict in index_to_attr.items():
    hdf5_filename = '{}_{}.hdf5'.format(param['datetime'],i)
    hdf5_file = h5py.File(hdf5_filename,'w')
    print('creating: {}'.format(hdf5_filename))
    # Add attributes
    for k, v in attr_dict.items():
        try:
            hdf5_file.attrs[k] = v
        except TypeError:
            hdf5_file.attrs[k] = json.dumps(v)

    # Add datasets
    for k, v in index_to_data[i].items():
        hdf5_file.create_dataset(k,data=np.array(v))
    hdf5_file.close()


