import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Read the CSV file into df
df = pd.read_csv('iris.csv')

def frequencyBar():
    # Plot the bar chart according to the frequency of species
    df['Species'].value_counts().plot(kind='bar', figsize=(8, 6), color=['r', 'g', 'b'])
    plt.title("Frequency Bar Graph")
    plt.xlabel("Species")
    plt.ylabel("Frequency of Species")
    plt.show()

def pcaAppliedGraph():
    # Perform PCA on the dataset
    X = df.iloc[:, 1:5].values
    X_std = StandardScaler().fit_transform(X)
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(X_std)
    principalDf = pd.DataFrame(data=principalComponents, 
            columns=['principal component 1', 'principal component 2'])
    finalDf = pd.concat([principalDf, df['Species']], axis=1)

    # Plot the PCA graph
    plt.figure(figsize=(10, 8))
    targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    colors = ['r', 'g', 'b']
    for target, color in zip(targets, colors):
        indicesToKeep = finalDf['Species'] == target
        plt.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                    finalDf.loc[indicesToKeep, 'principal component 2'],
                    c=color, s=50)
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.title('PCA Graph')
    plt.legend(targets)
    plt.show()

def distributionHistogramSepal():
    # Histogram for sepal length
    plt.figure(figsize=(7, 5))
    plt.hist(df['SepalLengthCm'], color='r')
    plt.title("Sepal Length Histogram")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Distribution Count")
    plt.show()

    # Histogram for sepal width
    plt.figure(figsize=(7, 5))
    plt.hist(df['SepalWidthCm'], color='g')
    plt.title("Sepal Width Histogram")
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Distribution Count")
    plt.show()

def distributionHistogramPetal():
    # Histogram for petal length
    plt.figure(figsize=(7, 5))
    plt.hist(df['PetalLengthCm'], color='b')
    plt.title("Petal Length Histogram")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Distribution Count")
    plt.show()
    # Histogram for petal width
    plt.figure(figsize=(7, 5))
    plt.hist(df['PetalWidthCm'], color='orange')
    plt.title("Petal Width Histogram")
    plt.xlabel("Petal Width (cm)")
    plt.ylabel("Distribution Count")
    plt.show()

# Invoke the functions to display the graphs
frequencyBar()
pcaAppliedGraph()
distributionHistogramSepal()
distributionHistogramPetal()
