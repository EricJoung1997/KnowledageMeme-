import numpy as np
import paddlehub as hub
from paddlehub.dataset.base_nlp_dataset import BaseNLPDataset

def predict(ZY):    
    inv_label_map = {val: key for key, val in reader.label_map.items()}

    # Data to be prdicted
    data = [ZY]

    index = 0
    run_states = cls_task.predict(data=data)

    results = [run_state.run_results for run_state in run_states]
    for batch_result in results:
        # get predict index
        batch_result = np.argmax(batch_result, axis=2)[0]
        for result in batch_result:
            return inv_label_map[result]
            index += 1

print(predict(['知识网络是形成企业动态能力的重要知识来源,这一网络具有动态性和根植性,网络的知识转移效率受到企业自身吸收能力、所转移的知识特性等多方面因素的影响,企业应建立知识网络管理机制、构建开放的知识网络,在获取外部知识的同时提高企业的学习能力。']))