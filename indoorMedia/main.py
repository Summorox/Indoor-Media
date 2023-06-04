from CoreAgent import CoreAgent

model_paths = {
    'face_proto': 'deployproto.prototxt',
    'face_model': 'res10_300x300_ssd_iter_140000_fp16.caffemodel',
    'age_proto': 'deploy_age.prototxt',
    'age_model': 'age_net.caffemodel',
    'gender_proto': 'deploy_gender.prototxt',
    'gender_model': 'gender_net.caffemodel',
}
characteristics = ['gender', 'age']
img_path = 'happy-friends-from-different-races-culture-laughing_166273-465.jpg'

core_agent = CoreAgent(model_paths, characteristics, img_path)
core_agent.run()