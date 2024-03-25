from flask import Flask
import time

app = Flask(__name__)

n = 350000
def fibonacci(n):
    """计算Fibonacci序列的第n项。"""
    starttime = time.time()
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    endtime = time.time()
    time_cost = f"{endtime-starttime}"
    return time_cost


@app.route('/predict')
def predict():
    # time.sleep(1)  # 模拟I/O延迟1秒
    tmp_res = fibonacci(n)  # 模拟CPU密集延迟，约1.2s
    return "OK"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=9111)