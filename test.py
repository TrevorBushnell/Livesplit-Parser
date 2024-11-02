from livesplit_parser import LivesplitData
from livesplit_parser import RunnerData
import matplotlib as plt

super64guy = LivesplitData('/Users/henrystone/Desktop/MyProjs/Hackathon2024/LivesplitParserWebApp/splits/super64guy_sm64_16star.lss', time_key="RealTime")
frobuddy = LivesplitData('/Users/henrystone/Desktop/MyProjs/Hackathon2024/LivesplitParserWebApp/splits/frobuddy_sm64_16star.lss', time_key="RealTime")
test_dict = RunnerData({'super64guy':super64guy, 'frobuddy':frobuddy})

fig = test_dict.plot_num_attempts_comp()

