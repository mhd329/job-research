import matplotlib as mpl
import matplotlib.pyplot as plt

# 한글 깨짐 방지

mpl.rcParams['font.family'] ='gulim'
mpl.rcParams['axes.unicode_minus'] = False

# 비율 리스트와 우대사항 종류 리스트 (나중에 높은 순서대로 정렬되게끔 개선해야 함, 임의로 입력해둔 상태)

ratio = []
labels = ['AWS, Docker 등\n클라우드 경험' , 'Javascript\nTypescript' , 'React\nVue' , 'Git\nGitHub' , 'Node.js' , 'Java' , 'Linux 계열 개발 지식' , 'Kotlin' , 'Go']

# 우대사항 언급 순위 사전 (key 1 부터 횟수가 많은 순서대로 정렬되게끔 개선해야함, 임의로 입력해둔 상태)

number_of_mentions =\
    {
    1 : 35, 2 : 32, 3 : 28,
    4 : 19, 5 : 15, 6 : 14,
    7 : 7, 8 : 3, 9 : 3
    }
    
# 원형 차트 선언

f = plt.figure(figsize=(12,9), frameon = False)

# 우대사항 전체 언급 횟수 계산기

total = 0
for i in range(len(number_of_mentions)):
    total += number_of_mentions[i+1]

# 소수점 세 자리에서 반올림, 두 자릿수까지 반영

ten = 4
pos = 10**ten

# 전체에서 각 언급 횟수 비율을 계산 후 소수점 자리수 반영

def convert_ranks_to_percentage(ranks):
    return (((ranks / total) * pos) + 0.5) // 1 / 100

# 언급 비율 리스트에 높은 순서대로(key 1 부터) 추가

for j in range(len(number_of_mentions)):
    ratio.append(convert_ranks_to_percentage(number_of_mentions[j+1]))

# 만들어진 비율 리스트에 따라 원형 차트 생성

wedgeprops={'width': 0.98, 'edgecolor': 'w', 'linewidth': 5}
plt.pie(ratio, labels=labels, autopct='%.2f%%', counterclock=False, wedgeprops=wedgeprops, textprops = {'fontsize':13})
plt.title('각 자격요건/우대사항\n언급된 횟수 비율')
# plt.show()

# 만들어진 원형 차트를 이미지화 하여 저장

f.savefig('piechart.png', bbox_inches='tight')