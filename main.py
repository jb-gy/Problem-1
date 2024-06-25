def max_sum_subarray(arr, window_size):
  window_sum = sum([arr[i] for i in range(window_size)])
  max_sum = window_sum


  for i in range(len(arr) - window_size):
      window_sum = window_sum - arr[i] + arr[i + window_size]
      max_sum = max(window_sum, max_sum)

  return max_sum


print(max_sum_subarray([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))
