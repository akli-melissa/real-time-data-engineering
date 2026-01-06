from cms import CountMinSketch

data = [('#ai', 100), ('#data', 50), ('#stream', 10), ('#python', 5)]
cms = CountMinSketch(d=5, w=1000)

for tag, freq in data:
    for _ in range(freq):
        cms.update(tag)

print('Estimates:')
for tag, true in data:
    est = cms.estimate(tag)
    print(tag, true, est, est - true)
