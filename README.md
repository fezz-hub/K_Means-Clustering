# K_Means-Clustering

## Overview

This project shows how to group data into **3 clusters** using a method called **K-Means clustering**.

At a high level, the program:

* Takes a set of points (each with two values)
* Starts with 3 initial “centers”
* Repeatedly groups points around the closest center
* Adjusts the centers until things stop changing
* Outputs a score (SSE) showing how tight the groups are

---

## Simple Explanation (Non-Technical)

Imagine you have 20 dots on a page.

1. You randomly place 3 markers (these are your starting centers).
2. Each dot goes to the **closest marker**.
3. You then move each marker to the **middle of its assigned dots**.
4. Repeat steps 2–3 until the markers stop moving.

At the end:

* Each marker represents a **cluster**
* Each dot belongs to one group
* The program calculates how “tight” these groups are

---

## What Problem This Solves

This algorithm helps answer:

> “How can we automatically group similar things together?”

Examples:

* Group customers with similar spending habits
* Group similar images
* Identify patterns in data without labels

---

## How the Code Works (Step-by-Step)

### 1. Data Setup

```python
data = np.array([...])
```

* A fixed list of 20 points
* Each point has 2 values (like coordinates)

---

### 2. Input Loop (Reading Starting Centers)

```python
for i in range(6):
    num = float(input().strip())
    numbers.append(num)
```

#### Simple explanation:

* The program asks for **6 numbers**
* These form **3 starting positions**:

  * (x1, y1)
  * (x2, y2)
  * (x3, y3)

#### Why this matters:

The starting points affect how good the final grouping will be.

---

### 3. Creating the Centers

```python
centers = np.array([
  [numbers[0], numbers[1]],
  [numbers[2], numbers[3]],
  [numbers[4], numbers[5]]
])
```

* Converts input into 3 actual points
* These are the “markers” used to form clusters

---

### 4. The Main Loop (Core of the Algorithm)

```python
while not np.array_equal(centers, prev_centers):
```

#### Simple explanation:

* Keep repeating until the centers **stop changing**
* This means the grouping is stable

---

## Inside the Loop (What Happens Each Cycle)

### A. Distance Calculation

```python
distance = np.sqrt(((data[:, np.newaxis, :] - centers[np.newaxis, :, :])**2).sum(axis=2))
```

#### Simple explanation:

* For every point:

  * Measure how far it is from each center
* This produces a table of distances

---

### B. Assigning Points to Clusters

```python
labels = np.argmin(distance, axis=1)
```

#### Simple explanation:

* Each point chooses the **closest center**
* That determines its cluster

---

### C. Updating Centers

```python
for j in range(3):
    cluster_points = data[labels == j]
```

#### Simple explanation:

* For each cluster:

  * Collect all points assigned to it
  * Move the center to the **average position**

#### If a cluster has no points:

```python
new_centers.append(prev_centers[j])
```

* Keep the old center (avoid errors)

---

### D. Repeat

* With new centers, the process repeats
* Stops only when nothing changes

---

## Final Step: Measuring Quality (SSE)

```python
sse += np.sum((cluster_points - centers[j]) ** 2)
```

### Simple explanation:

* Measures how far points are from their center
* Lower value = tighter clusters = better result

---

## Where This Can Be Used (Real-World)

### Easy to understand examples:

**Retail**

* Group customers based on buying habits

**Banking**

* Detect unusual transactions

**Healthcare**

* Group patients with similar symptoms

**Marketing**

* Segment audiences for campaigns

**Telecommunications**

* Understand user behavior patterns

---

## Industries That Benefit

* Finance
* Retail & E-commerce
* Healthcare
* Telecommunications
* Manufacturing
* Technology / AI

---

## Strengths

* Simple and fast
* Works well for clear groupings
* Easy to implement

---

## Limitations

* You must choose number of clusters (k = 3 here)
* Results depend on starting points
* Not ideal for complex or irregular shapes

---

## Summary

This project demonstrates how machines can:

* Automatically find patterns
* Group similar items
* Improve decision-making without labeled data
