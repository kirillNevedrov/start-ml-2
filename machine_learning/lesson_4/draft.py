import numpy as np
import pandas as pd


class GradientDescentMse:
    """
    Базовый класс для реализации градиентного спуска в задаче линейной МНК регрессии
    """

    def __init__(
        self,
        samples: pd.DataFrame,
        targets: pd.DataFrame,
        learning_rate: float = 1e-3,
        threshold=1e-6,
        copy: bool = True,
    ):
        """
        :param samples: матрица объектов
        :param targets: вектор (матрица с 1 столбцом) ответов
        :param learning_rate: параметр learning_rate для корректировки нормы градиента
        :param threshold: величина, меньше которой изменение в loss-функции означает
        :param copy: копировать сэмплы или делать изменения in-place (см. add_constant_feature)
        """
        self.iteration_loss_dict = {}
        self.samples = samples.copy().values if copy else samples.values
        self.targets = targets.values
        self.learning_rate = learning_rate
        self.threshold = threshold

    def add_constant_feature(self):
        """
        Метод для создания константной фичи в матрице объектов samples
        """
        self.samples = np.c_[self.samples, np.ones(self.samples.shape[0])]

    def calculate_mse_loss(self) -> float:
        """
        Метод для расчета среднеквадратической ошибки

        :return: среднеквадратическая ошибка при текущих весах модели : float
        """
        scalar_value = np.dot(self.samples, self.beta)
        scalar_value = scalar_value - self.targets
        scalar_value = scalar_value**2

        return np.mean(scalar_value)

    def calculate_gradient(self) -> np.ndarray:
        """
        Метод для вычисления вектора-градиента

        :return: вектор-градиент, т.е. массив, содержащий соответствующее количество производных по каждой переменной : np.ndarray
        """
        gradient = []

        for j in range(self.samples.shape[1]):
            d_ij = self.samples[:, j]
         
            gradient.append(2 * np.mean((np.dot(self.samples, self.beta) - self.targets) * d_ij))

        return np.array(gradient)

    def iteration(self):
        """
        Обновляем веса модели в соответствии с текущим вектором-градиентом
        """
        self.beta = self.beta - (self.learning_rate * self.calculate_gradient())

    def learn(self):
        """
        Итеративное обучение весов модели до срабатывания критерия останова
        """
        self.beta = np.zeros(self.samples.shape[1])

        iteration_number = 0
        self.iteration()
        self.iteration_loss_dict[iteration_number] = self.calculate_mse_loss()

        while True:
            iteration_number += 1
            self.iteration()
            self.iteration_loss_dict[iteration_number] = self.calculate_mse_loss()

            if (
                abs(
                    self.iteration_loss_dict[iteration_number]
                    - self.iteration_loss_dict[iteration_number - 1]
                )
                <= self.threshold
            ):
                break

data = pd.read_csv('C:\Git\start-ml\machine_learning\lesson_4\data.csv')
X = data.drop(['target'], axis=1)
Y = data['target']

GD = GradientDescentMse(samples=X, targets=Y)
GD.add_constant_feature()
GD.learn()