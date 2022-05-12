import json
from pprint import pprint


toefl_data = json.load(open("./toefl_type2_sample_v1-1.json"))
processed_data = []
idx = 0

for entity in toefl_data:
    for i in range(len(entity['edited_essay'])):
        ent = dict()
        ent['id'] = idx
        ent['question'] = entity['user_essay'][i]

        tags = entity['edited_tags'][i]
        ent['target'] = f'{len(tags)} {" ".join(tags)}'
        ent['answers'] = f'{len(tags)} {" ".join(tags)}'

        ctxs = []
        ctx = {"title": "idea_suggestions", "text":  " ".join(entity['prompt']['idea_suggestions'])}
        ctxs.append(ctx)
        ctx = {"title": "model_answer_text", "text":  " ".join(entity['prompt']['model_answer_text'])}
        ctxs.append(ctx)
        ctx = {"title": "question", "text":  " ".join(entity['prompt']['question'])}
        ctxs.append(ctx)
        ctx = {"title": "tips", "text":  " ".join(entity['prompt']['tips'])}
        ctxs.append(ctx)
        ctx = {"title": "user_essay", "text":  " ".join(entity['user_essay'])}
        ctxs.append(ctx)
        
        ent['ctxs'] = ctxs

        processed_data.append(ent)
        idx += 1

json.dump(processed_data[:4*(idx//5)], open("./toefl_type2_sample_v1-1_processed_tags_train.json", "wt"))
json.dump(processed_data[4*(idx//5):], open("./toefl_type2_sample_v1-1_processed_tags_eval.json", "wt"))