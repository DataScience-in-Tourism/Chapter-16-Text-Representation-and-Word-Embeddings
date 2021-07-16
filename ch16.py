import sys
from distutils.version import LooseVersion

import numpy as np
import pandas as pd
import nltk
import sklearn
import gensim
import tensorflow as tf
import tensorflow_hub as hub
import pytorch_transformers 
import torch
import spacy
import nlp
import glove

def check_versions():
    """
    check package version
    return: None
    """
    versions = {}
    ok = "(\u2713)"
    nok = "(\u2717)"
    
    v = ok if sys.version_info >= (3, 7) else nok
    versions['python'] = f'{sys.version_info.major}.{sys.version_info.minor} {v}'
    
    v = LooseVersion(np.__version__)
    versions['numpy'] = f'{v}' + (ok if v >= LooseVersion(r'1.17') else nok)
    
    v = LooseVersion(pd.__version__)
    versions['pandas'] = str(v) + (ok if v >= LooseVersion(r'1.0') else nok)
    
    v = LooseVersion(nltk.__version__)
    versions['nltk'] = str(v) + (ok if v >= LooseVersion(r'3.6') else nok)
    
    v = LooseVersion(sklearn.__version__)
    versions['sklearn'] = str(v) + (ok if v >= LooseVersion(r'0.23') else nok)
    
    v = LooseVersion(gensim.__version__)
    versions['gensim'] = str(v) + (ok if v >= LooseVersion(r'4.0') else nok)
    
    v = LooseVersion(tf.__version__)
    versions['tensorflow'] = str(v) + (ok if v >= LooseVersion(r'2.5') else nok)
    
    v = LooseVersion(hub.__version__)
    versions['tensorflow_hub'] = str(v) + (ok if v >= LooseVersion(r'0.12') else nok)
    
    v = LooseVersion(pytorch_transformers.__version__)
    versions['pytorch_transformers'] = str(v) + (ok if v >= LooseVersion(r'1.2') else nok)
    
    v = LooseVersion(torch.__version__)
    versions['pytorch'] = str(v) + (ok if v >= LooseVersion(r'1.8') else nok)
    
    v = LooseVersion(spacy.__version__)
    versions['spacy'] = str(v) + (ok if v >= LooseVersion(r'3.0') else nok)
    
    v = LooseVersion(nlp.__version__)
    versions['nlp'] = str(v) + (ok if v >= LooseVersion(r'0.4') else nok)
    
    v = LooseVersion(glove.__version__)
    versions['glove'] = str(v) + (ok if v >= LooseVersion(r'0.2') else nok)


    for version in versions:
        print(version, versions[version])



