import numpy as np

#array of datapoints
data = np.array([[0.22, 0.33],[0.45, 0.76],
[0.73, 0.39],[0.25, 0.35],[0.51, 0.69],
[0.69, 0.42],[0.41, 0.49],[0.15, 0.29],
[0.81, 0.32],[0.50, 0.88],[0.23, 0.31],
[0.77, 0.30],[0.56, 0.75],[0.11, 0.38],
[0.81, 0.33],[0.59, 0.77],[0.10, 0.89],
[0.55, 0.09],[0.75, 0.35],[0.44, 0.55]])

#read 6 numbers as initial centers for 3 clusters

numbers= []
for i in range(6):
    try:
        num = float(input().strip())
        numbers.append(num)
    except EOFError:
        break
    except ValueError:
        pass

# Initialize centers for 3 clusters 
centers = np.array([[numbers[0],numbers[1]],
[numbers[2],numbers[3]],[numbers[4],numbers[5]]])
#initialise previous centers to zeros for stopping condition
prev_centers = np.zeros_like(centers)

#stoping condition satisfued when centers do not change between iterations
while not np.array_equal(centers, prev_centers):
    prev_centers = centers.copy()

    #computing distace d(u,x)from each point to each center and assign to the nearest center
    distance = np.sqrt(((data[:, np.newaxis, :] -centers[np.newaxis, :, :])**2).sum(axis =2))
    labels = np. argmin(distance, axis = 1)
    
    #updat centers by calculating the mean of points assigned to each cluster
    new_centers = []

    #set range to 3 since k is 3
    for j in range(3):
      
      cluster_points = data[labels == j]
      if len(cluster_points) > 0:
        new_centers. append (cluster_points.mean (axis=0))
    
      #else if no points are assinged to a cluster, then the center remains unchanged
      else:
        new_centers.append(prev_centers[j])
    
    #update centers for next iteration
    centers = np.array(new_centers)

#calculate the sum of squared error SSE dor the final clusters
#using distance from each point to its assigned center
distance = np.sqrt(((data[:, np. newaxis,
:] - centers[np.newaxis,:, :]) ** 2). sum(axis=2))
labels = np.argmin(distance, axis=1)
sse = 0.0

for j in range (3):
  cluster_points = data[labels == j]
  if len (cluster_points) > 0:
    sse += np.sum((cluster_points - centers [j]) ** 2)

# Output SSE rounded to 4 decimal places
print(f"{sse: .4f}")