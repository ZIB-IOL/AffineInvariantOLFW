
def frank_wolfe(feasible_region,
                objective_function,
                step: dict,
                n_iters: int = 100,
                store_iterates: bool = False):
    """Performs Frank-Wolfe.

        Args:
            feasible_region:
                The type of feasible region.
            objective_function: Optional
                The type of objective function.
            step: dict
                A dictionnary containing the information about the step type. The dictionary can have the following arg-
                uments:
                    "step type": Choose from "open-loop", "exact", "line-search", "short-step".
                Additional Arguments:
                    For "open-loop", provide integer values for the keys "a", "b", "c" that affect the step type as
                    follows: a / (b * iteration + c)
                    For "line-search", provide an integer for the number of exhaustive search steps for the key
                    "number of iterations for line-search".
            n_iters: integer, Optional
                The number of iterations. (Default is 100.)
            store_iterates: bool, Optional
                (Default is False.)

        Returns:
            iterate_list: list
                Returns a list containing the iterate at each iteration.
            loss_list: list
                Returns a list containing the loss at each iteration.
            fw_gap_list: list
                Returns a list containing the FW gap at each iteration.
            x:
                Returns x, the final iterate of the algorithm
            x_p_list:
                Returns a list containing the values of ||x_t - p_t|| at each iteration.

        References:
            [1] "Marguerite Frank, Philip Wolfe, et al. An algorithm for quadratic programming. Naval research logistics
            quarterly, 3(1-2):95–110, 1956."
    """

    x = feasible_region.initial_point()
    loss_list = []
    fw_gap_list = []
    iterate_list = []
    x_p_list = []

    for i in range(0, n_iters):
        gradient = objective_function.evaluate_gradient(x)
        p_fw, fw_gap, x_p = feasible_region.linear_minimization_oracle(gradient, x)
        x_p_list.append(x_p)
        try:
            scalar = objective_function.compute_step_size(i, x, p_fw, gradient, step=step)
        except:
            break
        loss = objective_function.evaluate_loss(x)
        loss_list.append(loss)
        fw_gap_list.append(fw_gap)
        if store_iterates:
            iterate_list.append(x)
        x = (1 - scalar) * x.flatten() + scalar * p_fw.flatten()
    return iterate_list, loss_list, fw_gap_list, x, x_p_list
