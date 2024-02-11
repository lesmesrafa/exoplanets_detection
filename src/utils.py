from torch.utils.data import Dataset
from numpy import bincount, ndarray
import matplotlib.pyplot as plt
from seaborn import color_palette
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class CreateDataset(Dataset):
    def __init__(self, pandas_csv_file, transform=None):
        self.data = pandas_csv_file
        self.labels = self.data.iloc[:,0].values - 1
        self.features = self.data.iloc[:, 1:].values
        self.transform = transform
        
    def __len__(self):
        length = len(self.labels)
        return length
    
    def __getitem__(self, idx):
        label = self.labels[idx]
        feature  =self.features[idx]
        
        if self.transform:
            feature = self.transform(feature)
            
        sample = {"feature": feature, "label": label}
        return sample
    
def print_pie_chart(train_labels: ndarray, after_before: str) -> None:
    
    label_counts = bincount(train_labels)
    label_names = ['Not Exoplanet','Exoplanet']
    plt.figure(figsize=(8, 6))
    plt.title(f'Labels distribution in the Training Dataset {after_before} SMOTE')
    plt.pie(label_counts, labels=label_names, autopct='%1.1f%%', startangle=90, colors=color_palette('pastel'));
    
def plot_exoplanet_flux(train_dataset):
    fig = make_subplots(rows=2, cols=2, subplot_titles=("Star #0 (Exoplanet)", "Star #1 (Exoplanet)",
                                                        "Star #3000 (No-Exoplanet)", "Star #3001 (No-Exoplanet)"))

    fig.add_trace(go.Scatter(y=train_dataset.__getitem__(0)['feature']), row=1, col=1)
    fig.add_trace(go.Scatter(y=train_dataset.__getitem__(1)['feature']), row=1, col=2)
    fig.add_trace(go.Scatter(y=train_dataset.__getitem__(3000)['feature']), row=2, col=1)
    fig.add_trace(go.Scatter(y=train_dataset.__getitem__(3001)['feature']), row=2, col=2)

    for i in range(1, 5):
        fig.update_xaxes(title_text="Time", row=(i-1)//2 + 1, col=(i-1)%2 + 1)
        fig.update_yaxes(title_text="Flux", row=(i-1)//2 + 1, col=(i-1)%2 + 1)

    fig.update_layout(height=600, width=800, title_text="Exoplanets Flux vs No-Exoplanet Flux", showlegend=False)

    fig.show()


    
