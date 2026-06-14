import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np



class Plotter:

    def plot(self, report, r_2, num_parameters, /,
             *, train_colour="#FF0000", test_colour="#FFD900", slope_colour="#6CC4FE",
             x_label="x", x2_label="x2", y_label="y", on_close=None):
        """Dispatch to the 2D or 3D plot based on the number of features."""

        if num_parameters == 1:
            return self._plot_2d(report, r_2,
                          train_colour=train_colour,
                          test_colour=test_colour,
                          slope_colour=slope_colour,
                          x_label=x_label, y_label=y_label, on_close=on_close)
        elif num_parameters == 2:
            return self._plot_3d(report, r_2,
                          train_colour=train_colour,
                          test_colour=test_colour,
                          slope_colour=slope_colour,
                          x_label=x_label, x2_label=x2_label, y_label=y_label, on_close=on_close)
        else:
            return self._plot_predictions(report, r_2, slope_colour=slope_colour, points_colour=train_colour,on_close=on_close)


    def _plot_2d(self, report, r_2, /,
                 *, train_colour, test_colour, slope_colour, x_label, y_label, on_close=None):
        """Draw the graph in 2D."""
        X_train = np.array(report["x_train"]).flatten()
        X_test  = np.array(report["x_test"]).flatten()
        Y_train = report["y_train"]
        Y_test  = report["y_test"]
        coef      = report["coefficients"]
        intercept = report["intercept"]

        x_all  = np.concatenate([X_train, X_test])
        x_line = np.linspace(x_all.min(), x_all.max(), 300)
        y_line = coef * x_line + intercept

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.scatter(X_train, Y_train, color=train_colour, label="Train data",  alpha=0.7)
        ax.scatter(X_test,  Y_test,  color=test_colour,  label="Test data",   alpha=0.9)
        ax.plot(x_line, y_line, color=slope_colour, linewidth=2,
                label=f"Regression line (R²={r_2:.2f})")
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title("Linear Regression (2D)")
        ax.legend()
        plt.tight_layout()
        if on_close:
            fig.canvas.mpl_connect('close_event', on_close)
        plt.show(block=False)
        return fig

    def _plot_3d(self, report, r_2, /,
                 *, train_colour, test_colour, slope_colour, x_label, x2_label, y_label, on_close=None):
        """Draw the graph in 3D."""

        X_train = np.array(report["x_train"])
        X_test  = np.array(report["x_test"])
        x1_train, x2_train = X_train[:, 0], X_train[:, 1]
        x1_test,  x2_test  = X_test[:, 0],  X_test[:, 1]
        Y_train = report["y_train"]
        Y_test  = report["y_test"]
        coefs = report["coefficients"]
        intercept = report["intercept"]

        x1_all  = np.concatenate([x1_train, x1_test])
        x2_all  = np.concatenate([x2_train, x2_test])
        X1, X2  = np.meshgrid(np.linspace(x1_all.min(), x1_all.max(), 30),
                               np.linspace(x2_all.min(), x2_all.max(), 30))
        Y_plane = coefs[0] * X1 + coefs[1] * X2 + intercept

        fig = plt.figure(figsize=(10, 7))
        ax  = fig.add_subplot(111, projection="3d")
        ax.scatter(x1_train, x2_train, Y_train, color=train_colour, label="Train data", alpha=0.7, s=30)
        ax.scatter(x1_test,  x2_test,  Y_test,  color=test_colour,  label="Test data",  alpha=0.9, s=30)
        alpha: float = 0.45

        ax.plot_surface(X1, X2, Y_plane, alpha=alpha, color=slope_colour)
        proxy = Patch(color=slope_colour, alpha=alpha, label=f"Regression plane (R²={r_2:.2f})")

        ax.legend(handles=[*ax.get_legend_handles_labels()[0], proxy])
        ax.set_xlabel(x_label)
        ax.set_ylabel(x2_label)
        ax.set_zlabel(y_label)
        ax.set_title("Linear Regression (3D)")
        plt.tight_layout()
        if on_close:
            fig.canvas.mpl_connect('close_event', on_close)
        plt.show(block=False)
        return fig
    


    def _plot_predictions(self, report, r_2, slope_colour, points_colour, on_close=None ):
        """
        Actual vs Predicted plot.
        Works with any number of features.
        """

        y_test = report["y_test"]
        y_pred = report["y_pred"]
        num_features = report["x_train"].shape[1]

        fig, ax = plt.subplots(figsize=(8, 5))

        ax.scatter(y_test, y_pred, alpha=0.7, color=points_colour)

        minimum = min(y_test.min(), y_pred.min())
        maximum = max(y_test.max(), y_pred.max())

        ax.plot(
            [minimum, maximum],
            [minimum, maximum],
            linestyle="--",
            linewidth=2,
            label=f"Ideal fit (R²={r_2:.2f})",
            color=slope_colour
        )

        ax.set_xlabel("Actual values")
        ax.set_ylabel("Predicted values")
        ax.set_title(f"Actual vs Predicted ({num_features} features)")
        ax.legend()

        plt.tight_layout()

        if on_close:
            fig.canvas.mpl_connect("close_event", on_close)

        plt.show(block=False)

        return fig