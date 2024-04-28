import json

with open('Data\WLASL_v0.3.json', 'r') as f:
    config = json.load(f)
    
    tags = config[1]
    tags = [x['gloss'] for x in tags]
    
    vedio_id = config[0]['instances']
    vedio_id = [x['video_id'] for x in vedio_id]
    
    for x,y in zip(tags, vedio_id):
        print(x,y)
    # print(config)
    