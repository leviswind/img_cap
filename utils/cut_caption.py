# coding=utf-8
import json
import thulac
import pdb
import os

base_path = '/media/dl/expand/ai_challenger_caption_train_20170902'

with open(os.path.join(base_path, 'caption_train_annotations_20170902.json'), 'r') as f:
    data = json.load(f)
# ensure that there are five captions for each image
for _, cap in enumerate(data):
    assert len(cap['caption']) == 5

# using thulac to cut words
thu1 = thulac.thulac(seg_only=True)
samples = data[0]['caption']
for i, sample in enumerate(data):
    caps = sample['caption']
    cut_caps = []
    for _, cap in enumerate(caps):
        # cut words
        text = thu1.cut(cap.encode('utf-8'), text=True)
        text = unicode(text, 'utf-8')
        cut_caps.append(text)
    # print(data[0])
    # update the dict according to the cut words
    data[i].update(caption=cut_caps)
    # print(data[0])
    # pdb.set_trace()
with open(os.path.join(base_path, 'caption_train_annotations_cut.json'), 'w') as f:
    json.dump(data, f)
