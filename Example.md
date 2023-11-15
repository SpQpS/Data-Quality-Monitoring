<h1 align="center">Data Quality Monitoring Example</h1>

**Input Data:**

| Sr. No | Values |
| :---: | :---: |
| 1 | 10 |
| 2 | 8 |
| 3 | 12 |
| 4 | 14 |

**1. Mean Calculation:**
- Mean = ```(10+8+12+14)/4``` = ```11```

​
**2. Standard Deviation Calculation:**
 <h1 align="left"><img src="https://github.com/SpQpS/Data-Quality-Monitoring/assets/87906226/c90acd39-d573-4f74-9243-3b4b9197f550" width="300" height="75"></h1>


**3. Anomaly Detection Threshold:**
 <h1 align="left"><img src="https://github.com/SpQpS/Data-Quality-Monitoring/assets/87906226/eb45f29a-4af4-456d-8ccd-e156fb11be08" width="200" height="65"></h1>

**Checking for Anomalies:**
- For 10:
  - Upper Bound = ```11 + 6.708 ≈ 17.708```
  - Lower Bound = ```11− 6.708 ≈ 4.292```

```10 is within the range (no anomaly).```

- For 8:
  - Upper Bound = ```11+6.708 ≈ 17.708```
  - Lower Bound = ```11−6.708 ≈ 4.292```

```8 is within the range (no anomaly).```

- For 12:
  - Upper Bound = ```11+6.708 ≈ 17.708```
  - Lower Bound = ```11−6.708 ≈ 4.292```

```12 is within the range (no anomaly).```

- For 14:
  - Upper Bound = ```11+6.708 ≈ 17.708```
  - Lower Bound = ```11−6.708 ≈ 4.292```

```14 is within the range (no anomaly).```

- For 30:
  - Upper Bound = ```11+6.708 ≈ 17.708```
  - Lower Bound = ```11−6.708 ≈ 4.292```

```30 is outside the range (anomaly detected).```

**Conclusion:**
- The script would detect an anomaly for the value 30 because it falls outside the expected range based on the calculated mean and standard deviation.
