import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def send_request():
    """发送请求到Flask应用的/predict端口并返回响应结果。"""
    response = requests.get('http://127.0.0.1:9111/predict')
    return response.text

def main():
    # 开始计时
    start_time = time.time()

    # 使用线程池执行n个请求
    max_workers = 5
    tasks = 30
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(send_request) for _ in range(tasks)]

        # 等待所有请求完成，并打印结果
        print(f"Submited {len(futures)} tasks...")
        for future in as_completed(futures):
            response = future.result()
            print(response)

    # 结束计时并计算总耗时
    total_time = time.time() - start_time
    print(f"全部接口请求完成所需耗时: {total_time:.2f}秒")

if __name__ == '__main__':
    main()