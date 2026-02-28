with open("input.txt", "r") as f:
	start, day, end = f.read().strip().split("\n")
from datetime import datetime
start = datetime.strptime(start, "%Y-%m-%d")
end = datetime.strptime(end, "%Y-%m-%d")
days = ["Mahomesday","Jonesday","Kelceday","McDuffieday","Humphreyday","Thuneyday","Smithday"]
cur = days.index(day)
delta = end - start
cur = (cur + delta.days) % 7
print(days[cur], delta.days-1)