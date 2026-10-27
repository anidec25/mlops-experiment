"""Dummy training pipeline: load data -> preprocess -> train -> evaluate."""
import random


def load_data(n=100):
    return [(x, 2 * x + random.gauss(0, 0.1)) for x in range(n)]


def preprocess(data):
    split = int(len(data) * 0.8)
    return data[:split], data[split:]


def train(train_data, lr=1e-4, epochs=50):
    w = 0.0
    for _ in range(epochs):
        for x, y in train_data:
            w -= lr * 2 * (w * x - y) * x
    return w


def evaluate(w, test_data):
    return sum((w * x - y) ** 2 for x, y in test_data) / len(test_data)


def run():
    train_data, test_data = preprocess(load_data())
    w = train(train_data)
    print(f"weight={w:.3f} mse={evaluate(w, test_data):.4f}")


if __name__ == "__main__":
    run()
