# Workshop 1: Modellen in de cloud

© Auteur: Rik Jansen, bewerkt door Gillian Schmitz

**Doel van de workshop**
Het doel van deze workshop is om duidelijk te maken wat jullie in deze lessenserie gaan leren. Deze workshop beginnen we met wat over uitleg AzureML en over het hosten van machinelearningmodellen in de cloud. Deze lessenserie laat zien hoe je van een lokaal model (op je laptop) naar een bruikbaar model in de cloud kan gaan, net zoals dat in een echt bedrijf gebeurt. 



## 1. Van lokale experimenten naar een bruikbaar model in de cloud
Het gaan van een lokaal experiment naar een model dat in de cloud staat en overal bereikbaar is gaat helaas niet vanzelf. Deze workshop neemt je mee in de eerste stappen om een model te trainen in AzureML. 


### 1.1 Waarom gebruiken we de cloud?
Het gebruiken van de cloud heeft verschillende voordelen:

- **Reproduceerbaarheid** - Omdat iedereen gebruik maakt van dezelfde server (in deze lessen is die van microsoft), heeft iedereen ook precies dezelfde data en environment. Als het bij 1 iemand werkt, werkt het bij de rest ook.
- **Makkelijk deelbaar** - Je kunt overal inloggen en je notebooks delen. Als je een computer met een internetverbinding hebt kun je al werken. Ook kun je makkelijk rollen geven aan gebruikers, alleen de mensen die het mogen zien/bewerken, kunnen dat!
- **Makkelijk te testen** - In AzureML en andere vergelijkbare services zijn er tools beschikbaar die automatisch je modellen en de performance van die modellen bijhouden. Je hoeft dus veel minder moeite te doen om telkens plots te maken van de standaard prestaties. 
- **Niet meer afhankelijk van 1 laptop** - Als je een model zou hosten op 1 laptop ben je erg afhankelijk van die laptop. Als er ook maar iets fout gaat betekent het ook dat je model niet meer werkt. Door de cloud te gebruiken zorgt de aanbieder voor jou dat je model altijd te gerbuiken is. 

Maar naast de voordelen zijn er ook nadelen:

- **Kosten** - Aan alles wat je gebruikt van AzureML (of andere cloud aanbieders) zitten kosten verbonden. 
- **Het klaarzetten kost tijd** - Het klaarzetten van alles kost tijd. Je moet bijvoorbeeld rekening houden met wie er allemaal toegang mogen hebben, en je moet rekening houden met de resources die je gebruikt, zoals opslag en snelheid van de server die je leent. Die kosten namelijk allemaal geld. Je moet dus inschatten wat je nodig hebt, niet te veel, maar ook niet te weinig. 


### 1.2 Nieuwe punten waar je rekening mee moet houden
Omdat je nu een model aan het trainen bent in de cloud moet je nog wel rekening met nieuwe dingen houden. 

- Zo moet je een **environment** klaarzetten. Als je op eigen laptop werkt moet je een environment klaarzetten met packages. Hier werkt dat net zo, alleen hoef je maar 1 environment te maken. Die is precies hetzelfde voor iedereen, dus dan heb je geen last meer van: _"Maar op mijn laptop werkt hij wel gewoon"_.
- Daarnaast run je de code op een **cluster**. Je leent in principe een klein stukje van een computer van Microsoft. Afhankelijk van de grootte en snelheid van het deel dat je leent, betaal je ook meer of juist minder. Je moet dus van tevoren goed bedenken wat je nodig hebt. 
- Na het trainen van het model moet je het model **registreren**. Simpel gezegd maak je van je getrainde model een echt model dat bruikbaar is, hier ga je dus van een bestand dat alleen maar in de cloud staat, naar een bruikbaar model dat je kunt aanroepen.
- Zodra je je model af hebt, kun je het **deployen**. Hiermee zet je het model klaar voor gebruik, waar dan ook. Hiermee kun je met alleen maar 1 request een prediction maken met het model, de output van het model krijg je dan terug. Het model maak je bereikbaar voor anderen door een **endpoint** eraan toe te voegen.


### 1.3 Waarom AzureML
AzureML is slechts 1 van de mogelijke opties die je kunt overwegen. Wel is het 1 van de populairste in het bedrijfsleven en heeft het alle functionaliteiten die je zou kunnen wensen voor zo'n service. Als je weet hoe AzureML werkt, leer je de andere opties ook snel. 

Een paar alternatieven voor AzureML zijn:
- Databricks
- Amazon SageMaker
- Google Vertex AI
- En nog veel meer

Ook is het mogelijk om verschillende diensten samen te gebruiken. Bijvoorbeeld kun je voor opslag Azure gebruiken, om dan de notebook/modellen te trainen in Databricks. Het is allemaal afhankelijk van de prijs en de features die je zoekt. 

### 1.4 Begrippen
Omdat er veel nieuwe begrippen bij het werken met Azure komen kijken staat hieronder een tabel waar je makkelijk de definities kunt opzoeken. Dat maakt het net wat makkelijker om alles te volgen. 

#### 1.4.1 Algemene begrippen
|Begrip|Uitleg|
|---    |---|
|**Azure**          |De volledige koepelnaam voor het alle cloud-producten die Microsoft aanbiedt.|
|**Azure Portal**   |Het portaal van Azure, hier kun je makkelijk navigeren naar de verschillende diensten binnen Azure.|
|**AzureML**        |Het platform die wordt gebruikt voor alles rondom Machine learning, dit kan zijn: het managen van je data, compute clusters en notebooks|

#### 1.4.2 AzureML specifieke begrippen
|Begrip|Uitleg|
|---    |---|
|**Cluster/Managed Compute**|Dit het deel van de computer die je leent van Microsoft voor het runnen van je code. Hoe meer je leent hoe meer je betaalt. Voor een nadere uitleg zie: [Hoofdstuk 4. Managed compute maken](#4-stap-2-managed-compute-maken)|
|**AzureML Studio** |Dit is het deel van AzureML waarin je code kunt schrijven in notebooks en andere acties uit kunt voeren die met machine learning te maken hebben.|
|**Registreren**    |Voordat je een model wil gaan **Deployen** moet je het model registreren. Dat houdt in dat je van een model dat na het trainen in je lokale opslag staat, een compleet model van maakt en die opslaat zodat die in Azure kan worden gebruikt. Dit heet een **Model Asset**|
|**Model Asset**| Een Model Asset is het object dat je getrainde model bevat. Na het trainen en opslaan van een model, kun je jouw model **Registreren**. Na de Registratie is je model een Model Asset geworden en kun je het gebruiken voor bijvoorbeeld **deployment** of in samenwerking met andere modellen. |
|**Deployen**       |Deployment is het proces waarin je bijvoorbeeld een model online zet om te gebruiken. Dit gaat via een **Endpoint**. Het model dat wordt gedeployed moet een **Model Asset zijn**. |
|**Endpoint**       |Een endpoint kun je zien als een ingang van je model (of iets anders) dat je gedeployed hebt. Het is net zo als het bezoeken van een website, hiervoor heb je een adres nodig en vaak een wachtwoord/sleutel. Hiermee kun je toegang krijgen tot een model op de cloud met maar 1 call naar een server.|

#### 1.4.3 Infrastructuur specifieke begrippen
|Begrip|Uitleg|
|---    |---|
|**ClickOps**       |Clickops is het begrip van het klaarzetten van infrastructuur (zoals data en compute clusters) door gebruik te maken van de **Azure Portal** en **Azure ML**. Dit klikken is niet efficient omdat het fout gevoelig is, maar voor de eerste keer wel makkelijker dan wanneer je daarvoor scripts gebruikt (**IaC**), vandaar de naam.|
|**Infrastructure as Code (IaC)**| In tegenstelling tot bij **ClickOps** zet je hier de infrastructuur niet klaar door te klikken, maar door hier code voor te schrijven. Dit kan in het begin ingewikkelder zijn, maar is minder foutgevoelig dan klikken en het is te automatiseren en dus ook schaalbaar en herhaalbaar.|
|**Infrastructuur** |Verwijst naar de fundamentele (vaak door hardware ondersteunde) middelen die nodig zijn om machine learning-taken uit te voeren, zoals compute clusters, opslag, netwerken en databases. In grote bedrijven liggen taken rond het opzetten en onderhouden van de infrastructuur bij de MLOps Engineer / Cloud Engineer.|
|**ML application** |Dit zijn de daadwerkelijke machine learning-modellen, code en bedrijfslogica die bovenop de infrastructuur draaien. Dit omvat trainingsscripts, inferentiediensten en API’s die voorspellingen leveren. Dit kun je dus zien als de instellingen en data die over de **infrastructuur** loopt. Dit wordt dus gemaakt door de Data Scientist / ML Engineer.|
|**Tenant**         |Dit is de organisatie waar je inzit. Voor nu betekent dat dus de HU. Jouw schoolmail valt hier dan onder.|
|**Resource Group** |Dit is een groep van Azure componenten. Bijvoorbeeld kun je jouw AzureML Workspace, opslag en compute cluster groeperen om overzicht te houden en kosten in de gaten te houden.|

---
## 2. Workshop outline
In deze workshop behandelen we twee belangrijke concepten in AzureML:

- **Het trainen van een model in AzureML Studio:** We maken een cluster aan in AzureML waarmee we code kunnen runnen. Daarna gaan we in AzureML Studio notebooks maken en een model trainen.
- **Het deployen van een model:** Het model dat we hebben getraind zetten we online en zorgen we ervoor dat we live voorspellingen kunnen maken a.d.h.v. een HTTP API. 

Dit bestaat uit de volgende stappen:

1. **Handmatig AzureML resources toewijzen (met ClickOps)**  
    Hier maken we een nieuwe Workspace aan in AzureML en alles wat daarbij komt kijken in de Azure Portal

2. **Een managed compute maken**
    Hier gaan we een compute cluster maken. Daarbij vragen we om een stukje computer van Azure waar wij onze code op kunnen runnen.

3. **Een scikit-learn model trainen**
    Als we een cluster en onze data hebben klaargezet kunnen we een scikit-learn model trainen. Dit gaat op de manier hoe we het al kennen, alleen i.p.v. een jupyter notebook gebruiken we een AzureML Studio notebook.

4. **Het model registreren**
    In deze stap registreren we het model. Dit is de stap van het gaan van een model in het geheugen van je notebook naar een model dat bruikbaar is in de Azure omgeving.

5. **Het model deployen naar een endpoint**
    Als we het model hebben geregistreerd kunnen we het deployen zodat het model beschikbaar is online. 
6. **Het testen van de endpoint**
    Met het model online hoeven we alleen nog te kijken of het mogelijk is om een voorspelling te doen via de endpoint. 


---


## 3. Stap 1: Resources toewijzen met ClickOps

> **⚠ BELANGRIJK:** De resources die je leent kosten geld. In je licentie zit maar een beperkt tegoed. Je moet hier dus zuinig mee omgaan. Hieronder staat aangegeven hoe je hier mee om moet gaan en wat je moet doen om te voorkomen dat ineens al je tegoed op is. Dit gaat namelijk makkelijker dan je denkt. Dit gebruiken we nu niet, maar om de kosten in de toekomst in te schatten kun je het volgende gebruiken: [Microsoft's Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) en [Azure Machine Learning pricing details](https://azure.microsoft.com/en-us/pricing/details/machine-learning/).


### 3.1 Azure structuur en toegang
Azure maakt gebruik van **Role-Based Acces Control (RBAC)**, dit is de functionaliteit waar je verschillende rollen met verschillende rechten aan gebruikers kunt toewijzen. 

Als je de rechten van wie er allemaal mee mogen werken gaat veranderen  is het handig om even de [begrippen van infrasctructuur](#143-infrastructuur-specifieke-begrippen) door te nemen. 


### 3.2 AzureML Workspace klaarzetten
Een Azure Machine Learning workspace is de centrale plek in Azure waar je al je machine learning spullen en taken beheert. Zie het als een besturingspaneel dat alles met elkaar verbindt:

- **Datasets and data stores**
- **Managed compute** (compute- instances, -clusters, -endpoints)
- **Environments en dependencies**
- **Geregistreerde modellen**
- **Jobs en pipeline runs**

Alles wat je in AzureML doet gebeurt binnen zo’n workspace. Het is één plek om je middelen te organiseren, beveiliging in te stellen en activiteiten in de gaten te houden.

Om te beginnen maken we een workspace, hiervoor kan je de guide hieronder gebruiken. Je hoeft alleen het eerste deel van de guide te gerbuiken, het toewijzen van een managed compute staat in deze workshop beschreven. 
[ClickOps guide from Microsoft](https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources?view=azureml-api-2)

> **Resource Provider Error**: Soms krijg je foutmeldingen over “Resource Providers”. Zet dan AzureML als Resource Provider aan in je Azure-abonnement. Zie de volgende links voor oplossingen:
 [enable AzureML as a Resource Provider](https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/error-register-resource-provider?tabs=azure-portal#solution) of deze [ Azure Q&A thread](https://learn.microsoft.com/en-us/answers/questions/2129910/resource-provider-(n-a)-isnt-registered-with-subsc).


---


## 4. Stap 2: Managed Compute maken
Een **Managed Compute** in AzureML is een deel van de server van azure dat je leent om bijvoorbeeld je code te runnen. Een managed compute heeft verschillende vormen, welke je moet gebruiken is afhankelijk van waarvoor je het wil gebruiken:
- **Compute Instances (ookwel Personal Compute)** → Dit kun je zien als 1 (stukje van een) computer. Dit kun je net zo gebruiken als je eigen laptop. Wij gaan dit vooral gebruiken om modellen te trainen in een jupyter notebook. 
- **Compute Clusters** → Een cluster bestaat uit meerdere machines (of VM's). Deze kunnen automatisch op of af schalen als er veel of weinig gebruik van wordt gemaakt en als 1 VM uitvalt zal automatisch een andere het overnemen. Hierop kun je je modellen draaien die toegankelijk moeten zijn voor anderen. 

Azure zorgt voor: besturingssysteem, netwerk, opschalen, gebruikersbeheer en monitoring. Alles werkt direct samen met je AzureML workspace, zodat je op één plek modellen kunt trainen, opslaan en publiceren.

Zometeen gaan we een Compute Instance maken. Deze is gekoppeld aan één gebruiker en is dus niet bedoeld voor gedeeld of automatisch gebruik.

Zo’n Compute Instance bevat standaard:
- Populaire ML-bibliotheken (zoals scikit-learn, pandas, numpy)
- Geïntegreerde Python-omgevingen (Conda)
- Vooraf geïnstalleerde tools zoals JupyterLab, VS Code Server en een terminal
- Directe koppeling met de AzureML SDK en je workspace-resources

Het is eigenlijk een cloud-werkstation voor machine learning dat je via je browser gebruikt.

>In professionele MLOps-omgevingen worden deze rekenmiddelen vaak niet door Data Scientists zelf gemaakt, maar door MLOps Engineers of Cloud Engineers. Zo houd je beter grip op beveiliging, kosten en beheer.


### 4.1 Een Compute Instance maken (ClickOps)

1. Open [AzureML Studio](https://ml.azure.com/) en selecteer je workspace.

2. Klik op de blauwe **+ New** button rechts boven en klik op **Compute Instance**

3. Vul in:
   - **Name**: Kies een logische naam afhankelijk waarvoor je het gaat gebruiken, zoals: `ds-notebook-vm-test`.
   - **Virtual Machine type**: Selecteer **CPU**
   - **Virtual Machine Size**: Selecteer **Standard_DS11_v2**
     > Deze grootte heeft een goede balans van geheugen (14 GB) and cores (2 vCPUs) voor een lage prijs. Goed voor kleine experimenten dus.

4. Zoek onder de stappen: **Scheduling**, **enable idle-shutdown**.
   - Vul in dat de Compute Instance na **60 minutes** automatisch moet worden uitgeschakeld (of iets minder als je zuiniger wilt zijn).
   > ⚠ **Belangrijk**: Als je dit niet doet is er een grote kans dat binnen enkele dagen je tegoed op is, en dus niet meer de service kan gebruiken voor de rest van de maand. 

5. Dit zijn de enige dingen die je hoeft aan te passen, check nog 1 keer of je alles goed heb ingevuld en maak dan de Compute instance aan. Dit kan enkele minuten duren. 


---


## 5. Stap 3: Een Scikit-learn model trainen

### 5.1 AzureML en de Datastore
Als je in AzureML Studio werkt, worden notebooks en andere bestanden opgeslagen in een Datastore, dit is een beheerde opslagplek die aan je workspace is gekoppeld.
Notebooks komen standaard terecht in de `workspaceworkingdirectory` Datastore, die gebruikmaakt van een Azure Blob Storage-container (een stukje opslag op de Azure servers).
Hierdoor blijven je bestanden bewaard tussen sessies en kun je ze opnieuw gebruiken in taken en pipelines.

>💡 Je kunt alle Datastores in je workspace bekijken via Data > Datastores in het menu links in AzureML Studio.


### 5.2 Een Notebook maken

1. Navigeer in [AzureML Studio](https://ml.azure.com/) naar je workspace.
2. In het linker menu, selecteer **Notebooks**.
3. Klik **+files**, **Create new file**.
4. Selecteer **Notebook** in **File type** en vul een naam in zoals: `train-ames-housing.ipynb`.
5. De locatie hoef je niet te veranderen, de notebook zal standaard worden opgeslagen in de `workspaceworkingdirectory` Datastore.

### 5.3 Check je Compute en Kernel
Zodra je een notebook hebt gemaakt:

1. Gebruik de **Compute dropdown** om de notebook te koppelen aan de Compute Instance die je net hebt gemaakt. (bijv. `ds-notebook-vm-test`).
    - Als hij nog niet aanstaat kun je hem nu opstarten. Dit kan enkele minuten duren.
2. Zodra je Compute Instance aanstaat kun je rechts boven checken of je de **Python 3.10 - SDK v2** environment hebt geselecteerd. 
    - Deze heeft de meeste packages zoals numpy, pandas en sk-learn al voor je geinstalleerd. 

> Mocht je willen checken welke packages allemaal in environment zitten kun je het volgnde  **magic command** in een notebook cell uitvoeren: `%pip list`


---


## 6. Stap 4: De dataset uploaden
Zo gaan we een `.csv` uploaden in de standaard **`workspaceworkingdirectory`** Datastore, hier staat ook je notebook in. Nu doen we dit handmatig, maar je kunt je voorstellen dat in een professionele omgeving een script automatisch de data ophaalt en synchroniseerd naar een datastore zodat je altijd up-to-date data kunt gebruiken. 

Het bestand dat we gebruiken is `AmesHousing.csv`. 

Om het bestand te uploaden:

1. In AzureML Studio, ga naar **Notebooks**.
2. Navigeer naar de noteboook `train-ames-housing.ipynb` die je net hebt aangemaakt.
    - Als je nog je notebook open hebt staan kun je het tabblad van je notebook sluiten. 
3. Klik op **+files**, **Upload Files**.
4. Klik op **Click to browse and select file(s)** en navigeer naar de `.csv`. 
5. Klik op **I trust contents of this file** en klik **Upload**.

Nu kun je de dataset gebruiken vanuit je notebook: 
```py
import pandas as pd
pd.read_csv("AmesHousing.csv")
```


---


## 7. Stap 5: Een Random Forest model op de Ames Housing data trainen
Nu hebben we alles klaar staan om een model te trainen. Dit gaat op dezelfde manier die jullie al kennen, hier dus niets nieuws. We gebruiken hiervoor een dataset van huizen, hierbij staan de karakteristieken en prijs van de huis. Wij gaan een model trainen die op basis van de karakteristieken een voorspelling van de prijs kan maken.

Gebruik hiervoor de volgende code:

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import pickle
import json

# 1. Load dataset
df = pd.read_csv("AmesHousing.csv")

# 2. Select features and target
features = [
   'LotFrontage', 'GrLivArea', 'GarageArea',
   'Neighborhood', 'HouseStyle', 'ExterQual', 'MasVnrType',
   'YearBuilt', 'YrSold', 'OverallQual'
]
target = 'SalePrice'

df = df.dropna(subset=[target])  # remove rows with missing target
X = df[features]
y = df[target]

# 3. Train-test split (before preprocessing to avoid leakage)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123
)

# 4. Determine transformation parameters from training set
lotfrontage_mean = X_train['LotFrontage'].mean()
X_train['MasVnrType'] = X_train['MasVnrType'].replace("None", np.nan)
X_test['MasVnrType'] = X_test['MasVnrType'].replace("None", np.nan)
masvnrtype_mode = X_train['MasVnrType'].mode()[0]
categorical_cols = ['Neighborhood', 'HouseStyle', 'MasVnrType']
exterqual_mapping = {'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}
exterqual_na = 'TA'

# 5. Preprocess training set
X_train = X_train.copy()
X_train['HouseAge'] = X_train['YrSold'] - X_train['YearBuilt']
X_train['OverallQual'] = X_train['OverallQual'].clip(lower=1, upper=10)
X_train['LotFrontage'] = X_train['LotFrontage'].fillna(lotfrontage_mean)
X_train['MasVnrType'] = X_train['MasVnrType'].fillna(masvnrtype_mode)
X_train = pd.get_dummies(X_train, columns=categorical_cols)
X_train['ExterQual'] = X_train['ExterQual'].map(exterqual_mapping)
X_train['ExterQual'] = X_train['ExterQual'].fillna(exterqual_mapping[exterqual_na])

# Save the final column order for test set alignment
final_columns = X_train.columns.tolist()

# 6. Preprocess test set using same parameters
X_test = X_test.copy()
X_test['HouseAge'] = X_test['YrSold'] - X_test['YearBuilt']
X_test['OverallQual'] = X_test['OverallQual'].clip(lower=1, upper=10)
X_test['LotFrontage'] = X_test['LotFrontage'].fillna(lotfrontage_mean)
X_test['MasVnrType'] = X_test['MasVnrType'].fillna(masvnrtype_mode)
X_test = pd.get_dummies(X_test, columns=categorical_cols)
X_test['ExterQual'] = X_test['ExterQual'].map(exterqual_mapping)
X_test['ExterQual'] = X_test['ExterQual'].fillna(exterqual_mapping[exterqual_na])

# Align test columns to training columns
X_test = X_test.reindex(columns=final_columns, fill_value=0)

# 7. Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# 8. Evaluate model
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"R² Score: {r2:.2f}")
print(f"Mean Absolute Error: ${mae:,.0f}")

# 9. Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

```

Refresh je directory en check of het gelukt is om het model op te slaan. 


### 7.1 Transformation Parameters
We moeten naast het model ook de **Transformation parameters** onthouden. We kunnen niet zomaar de rauwe data in het model stoppen, omdat we tijdens het trainen hebben ook allemaal bewerkingen gedaan. De transformation parameters zijn de waardes die we nodig hebben om die stap van rauwe data naar input data te krijgen, voor het **preprocessen** dus. Dit zijn bijvoorbeeld de gemiddeldes (zoals `lotfrontage_mean`) of de mapping van de kwaliteit van *strings* naar *ints* (zoals `exterqual_mapping `). 

Later gaan we nog een script schrijven die zorgt dat de input die wordt gegeven ook de goede transformatie ondergaat zoals we tijdens het trainen hebben gedaan. Dit heet het **Scoring Script**, hier zo meer over. 

> In deze workshop hebben we de preprocessing code gekopieerd naar beide het train script en het scoring script, dit is natuurlijk niet optimaal. In de komende workshops wordt dit beter gedaan door gebruik te maken van nieuwe features. 


---


## 8. Step 4: Het model registreren
Zodra je jouw model hebt opgeslagen als een `.pkl` kun je het model registreren. 


### 8.1 Opgeslagen modellen
Voordat we het model kunnen registreren moeten we de het model in een andere plek opslaan dan dat hij nu is opgeslagen. AzureML kan namelijk alleen maar modellen registreren vanuit de **Azure Blob Storage**. Dit is een speciale opslag die gemaakt is voor grote- en ongestructureerde bestanden zoals modellen, datasets en logs. 

> Meer informatie over de verschillen tussen de twee soorten opslag van Azure vind je hier: [Azure Blob Storage vs Azure File Share](https://learn.microsoft.com/en-us/azure/storage/common/storage-introduction#azure-blob-storage-vs-azure-files).

Om hier tijdelijk omheen te werken downloaden we `model.pkl` lokaal, daarna stoppen we het handmatig in de juiste opslag. 


### 8.2 Download het `model.pkl` bestand

1. In AzureML Studio, navigeer naar het **Notebooks** venster.
2. Navigeer naar de juiste folder en zoek het `model.pkl` bestand.
3. Klik op de 3 puntjes naast het `model.pkl` bestand.
4. Selecteer **Download** om het model te downloaden naar je computer.


### 8.3 Het model registreren

Nu je het model hebt gedownload:

1. In AzureML Studio, navigeer naar **Models** onder **Assets** in het linker menu.
2. Klik op **+ Register** > **From local files**.
3. Vul in:
   - **Model type**: Kies **Unspecified type**
   - Klik **Browse, Browse file**, en upload `model.pkl`.
   - Onder **Model Settings** > **Name**: vul `ames-housing-model` in.
   - De rest kun je laten zoals het is

4. Klik **Register** om de registratie af te ronden.


---


## 9. Stap 5: Het model deployen naar een Real-time Endpoint
Nu we het model hebben geregistreerd kunnne we het model deployen naar een Endpoint. 


### 9.1 Scoring Script
Het deployen van een model bestaat uit verschillende stappen:
1. Laad het model uit de Model Asset
2. Het verwerken van inkomende requests naar het model
3. Voorspellingen ophalen uit het model
4. Formatteer de voorspelling en geef het terug in een HTTP response

Dit proces is verwerkt in een **scoring script**. Dit is een klein python bestand die uit twee functies bestaat: `init()` en `run(raw_data)`. In dit script is ook meteen de preprocessing verwerkt die ook plaatsvind voor het maken van de trainingsdata.

Hieronder staat een versie van `score.py`, dit bestand kun je gewoon lokaal maken:

```py
import json
import pickle
import pandas as pd
import os

# Globals for model and preprocessing parameters
model = None
xform_params = None

def init():
    global model, xform_params

    # Load model
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR", "."), "model.pkl")
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Init transformation parameters
    xform_params = {
        "lotfrontage_mean": 69.58426966292134, 
        "masvnrtype_mode": "BrkFace", 
        "categorical_cols": ["Neighborhood", "HouseStyle", "MasVnrType"], 
        "exterqual_mapping": {"Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5}, 
        "exterqual_na": "TA", 
        "final_columns": ["LotFrontage", "GrLivArea", "GarageArea", "ExterQual", "YearBuilt", "YrSold", "OverallQual", "HouseAge", "Neighborhood_Blmngtn", "Neighborhood_Blueste", "Neighborhood_BrDale", "Neighborhood_BrkSide", "Neighborhood_ClearCr", "Neighborhood_CollgCr", "Neighborhood_Crawfor", "Neighborhood_Edwards", "Neighborhood_Gilbert", "Neighborhood_IDOTRR", "Neighborhood_MeadowV", "Neighborhood_Mitchel", "Neighborhood_NAmes", "Neighborhood_NPkVill", "Neighborhood_NWAmes", "Neighborhood_NoRidge", "Neighborhood_NridgHt", "Neighborhood_OldTown", "Neighborhood_SWISU", "Neighborhood_Sawyer", "Neighborhood_SawyerW", "Neighborhood_Somerst", "Neighborhood_StoneBr", "Neighborhood_Timber", "Neighborhood_Veenker", "HouseStyle_1.5Fin", "HouseStyle_1.5Unf", "HouseStyle_1Story", "HouseStyle_2.5Fin", "HouseStyle_2.5Unf", "HouseStyle_2Story", "HouseStyle_SFoyer", "HouseStyle_SLvl", "MasVnrType_BrkCmn", "MasVnrType_BrkFace", "MasVnrType_Stone"]
    }


def preprocess(df):
    """Apply the same preprocessing as during training."""
    lotfrontage_mean = xform_params["lotfrontage_mean"]
    masvnrtype_mode = xform_params["masvnrtype_mode"]
    categorical_cols = xform_params["categorical_cols"]
    exterqual_mapping = xform_params["exterqual_mapping"]
    exterqual_na = xform_params["exterqual_na"]
    final_columns = xform_params["final_columns"]

    # Feature engineering
    df['HouseAge'] = df['YrSold'] - df['YearBuilt']
    df['OverallQual'] = df['OverallQual'].clip(lower=1, upper=10)
    df['LotFrontage'] = df['LotFrontage'].fillna(lotfrontage_mean)
    df['MasVnrType'] = df['MasVnrType'].fillna(masvnrtype_mode)
    df = pd.get_dummies(df, columns=categorical_cols)
    df['ExterQual'] = df['ExterQual'].map(exterqual_mapping)
    df['ExterQual'] = df['ExterQual'].fillna(exterqual_mapping[exterqual_na])

    # Align columns
    df = df.reindex(columns=final_columns, fill_value=0)

    return df


def run(raw_data):
    try:
        # Parse incoming request
        if isinstance(raw_data, str):
            data = json.loads(raw_data)
        else:
            data = raw_data

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Apply preprocessing
        X_new = preprocess(df)

        # Predict
        predictions = model.predict(X_new)

        # Return as JSON
        return json.dumps({"predictions": predictions.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})
```


### 9.2 Een Real-time Endpoint aanmaken
Nu we het scoring script hebben kunnen we het endpoint aanmaken:

1. In AzureML Studio, zoek **Endpoints** in het linker menu.
2. Selecteer het **Real-time endpoints** tabje en klik op **Create**
3. Selecteer het model dat je net geregistreerd hebt (`ames-housing-model`) en klik **Select**
4. In de **Endpoint** stap:
   - **Name**: Kies een logische naam, zoals: `ames-housing-endpoint-<yourname>`
   - **Authentication type**: Kies **Key-based** (is iets minder veilig dan de andere opties maar voor experimentatie het makkelijkst)
   - Laat de rest zoals het is
5. In de **Code + environment** stap:
   - **Select a scoring script for inferencing**: upload je `score.py` bestand
   - In het lijstje van **Curated environments**, zoek en selecteer _sklearn-1.5:26_ (of een nieuwere versie, klik op het bolletje links om het de environment te selecteren)
6. In de **Compute** stap:
   - **Virtual machine**, selecteer  __Standard_D2as_v4__
   - **Instance count**: Zet deze op **1**, meer heb je niet nodig

7. Laat de rest zoals het is en klik op **Create**

AzureML zal een endpoint toewijzen aan je model. Dit kan enkele tot 10 minuten duren.


## 10. Step 6: Het testen van je Endpoint
Als het goed is, is je model nu beschikbaar via een online endpoint. Nu kunnen we een HTTP request maken met inputdata, om vervolgens een voorspelling van het model te krijgen.


### 10.1 Authenticatie
Om te voorkomen dat iemand zonder toestemming je AzureML-endpoint gebruikt, is inloggen/authenticatie nodig.
Er zijn meerdere manieren om dat te doen (zoals via **Entra ID** of via **tokens**), maar in deze workshop gebruiken we **key-based authenticatie** omdat dat het makkelijkst is. Door de simpliciteit wordt deze ook het vaakst gebruikt in de experimentatie fase. Je kunt deze altijd nog aanpassen.

Bij key-based authentication gebruik je een geheime sleutel. Deze sleutel moet je meesturen in de HTTP request header.
Met deze sleutel krijgt iemand volledige toegang tot het endpoint, dus zorg dat je hem nooit openbaar deelt.


### 10.2 De Endpoint URL en Key 


1. Ga naar je **Endpoints** in AzureML Studio.
2. Klik op jouw endpoint die je net hebt gemaakt. 
3. Zoek het **Consume** tabje boven alle informatie blokken.
4. Hier moet je kopieren:
   - **REST endpoint URL**: De URL van je endpoint
   - **Primary key**: De authenticatie key die je nodig hebt voor je requests

> **Belangrijk**: Voordat je dit kan doen moet jouw endpoint **volledig** online staan. Dit kan even duren en je moet wachten tot je bij je status groene vinkjes hebt. Dan pas kun je het _Consume_ tabje vinden.


### 10.3 Een HTTP Request sturen naar je Endpoint
Hieronder staat een klein voorbeeld die je kunt gebruiken voor het sturen van een request. Vul de placeholders in met jouw URL en key:

```py
import requests
import json

# Replace with your actual endpoint URL and key
endpoint_url = "https://<your-endpoint-name>.westeurope.inference.ml.azure.com/score"
key = "<your-primary-key>"

# Sample input for Ames Housing model
sample_input = [
    {
        "LotFrontage": 65.0,
        "GrLivArea": 1500,
        "GarageArea": 480,
        "Neighborhood": "NAmes",
        "HouseStyle": "1Story",
        "MasVnrType": "BrkFace",
        "ExterQual": "Gd",
        "OverallQual": 7,
        "YearBuilt": 2005,
        "YrSold": 2010
    }
]


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {key}"
}

response = requests.post(endpoint_url, headers=headers, data=json.dumps(sample_input))

print("Prediction:", response.json())
```

Als je in je JSON response een getal hebt gekregen dan is het gelukt! Je hebt nu een model die je kunt aanroepen via een endpoint. Mocht het nog niet gelukt zijn, kijk nog even goed naar de vorige stappen of vraag het gerust aan iemand.

---

## 11. stap 7: Clean Up van je Resources
Als je de workshop hebt afgerond, is het belangrijk om je Azure-resources die we hebben aangemaakt op te ruimen. Zo voorkom je onnodige kosten.

### 11.1 Verwijder Compute en Endpoints

1. **Verwijder Endpoints**
   - Ga naar **Endpoints** in AzureML Studio..
   - Selecteer alle endpoints en klik op **Delete**.

2. **Stop en verwijder Compute Instances**
   - Ga naar **Compute** > **Compute instances**.
   - Stop alle instances die nog live zijn via het **Stop** knopje.
   - Klik **Delete** om ze te verwijderen.

3. **Verwijder Compute Clusters** (als je die hebt)
   - Ga naar **Compute** > **Compute clusters**.
   - Selecteer je cluster(s) en klik **Delete**.


### 11.2 Verwijder de hele Resource Group
Om alles in 1 keer te verwijderen kun je ook de gehele **Resource Group** verwijderen:

1. Ga naar de [Azure Portal](https://portal.azure.com/).
2. Navigeer naar **Resource Groups** in het linker menu.
3. Klik op de resource group om deze te openen.
4. Klik **Delete resource group** aan de bovenkant van de informatie over de resource group.
5. Typ de naam van de resource group in het vlak en klik **Delete**.

> **Note:** de resource group zelf brengt geen kosten met zich mee. Alleen de items in je resource group kosten geld, vaak ook als je niet worden gebruikt. De AzureML workspace zelf kan ook nog geld kosten al is het niet super veel. Om ervoor te zorgen dat het niet uit de hand loopt:
> Zorg ervoor dat je altijd je endpoint verwijderd als je het niet meer gerbuikt voor de rest van de dag. De rest is het niet heel erg als je het laat staan als je het de volgende dag weer gaat gebruiken, maar je kunt nooit te voorzichtig zijn. 


## 12. Recap en volgende stappen
In deze workshop zijn de eerste stappen gezet naar het maken van een ML systeem zoals de profs dat doen. Je hebt:

- Geleerd wat AzureML is en wat je er mee kunt
- De voordelen van het gebruiken van AzureML tegenover een lokaal project
- Geleerd hoe je een **managed compute** kunt opzetten
- Geleerd over **Datastores** in Azure
- Je weet hoe je een model kunt trainen in AzureML Studio
- Je kunt het model registreren, en deployed naar een real-time endpoint


### 12.1 Volgende workshop: Modular Workflows en Pipelines
In de volgende workshop ga je verder dan notebooks en handmatige stappen.

Je bouwt een modulaire pipeline die het hele modelproces bevat: data splitsen, data prep, trainen, registreren, deployen en testen.
Elke stap wordt een modulair en herbruikbaar onderdeel. De hele pipeline draait op beheerde compute en start met één CLI- of SDK-commando.

