def calc_running_average(data_points, data_points_till_now, old_average):
	if(len(data_points) == data_points_till_now): return data_points
	data_points[data_points_till_now] = (old_average * data_points_till_now + data_points[data_points_till_now]) / (data_points_till_now + 1)
	data_points_till_now += 1
	return calc_running_average(data_points, data_points_till_now, data_points[data_points_till_now - 1])



if __name__ == "__main__":
	print(calc_running_average([4, 4, 4, 4, 4], 0, 0))
	print(calc_running_average([5, 1, 19, 3], 0, 0))
	print(calc_running_average([2, 3, 4, 5, 6, 7], 0, 0))
	print(calc_running_average([8], 0, 0))