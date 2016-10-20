"""Dataset loader helpers. This file collects everything related to downloading
and organizing CheML and other open datasets for computational chemistry."""
import os
import urllib2

def get_data_dirs(data_dir=None):
    """Returns a priority list of folders where to search for a dataset.
    
    If `data_dir` is specified, this will have highest priority. The list is
    as follows:

    1. data_dir if specified
    2. the environment variable CHEML_SHARED_DATA if specified
    3. the environment variable CHEML_DATA if specified
    4. $HOME/CheML_data
    """

    paths = []


    cheml_shared_data = os.environ.get("CHEML_SHARED_DATA", None)
    cheml_data = os.environ.get("CHEML_DATA", None)
    home_data_folder = os.path.expanduser("~/cheml_data")

    if data_dir is not None:
        paths.append(data_dir)
    if cheml_shared_data is not None:
        paths.append(cheml_shared_data)
    if cheml_data is not None:
        paths.append(cheml_data)
    paths.append(home_data_folder)

    return paths



HF_URL_BASE = ("https://raw.githubusercontent.com/SamKChang/"
                "QM_wavelet/master/data/")

dataset_info = dict(
    HF2=("HF/HF2.pkl", HF_URL_BASE + "data_m2.pkl"),
    HF3_1K=("HF/HF3_1K.pkl", HF_URL_BASE + "data_m3.pkl"),
    HF4_1K=("HF/HF4_1K.pkl", HF_URL_BASE + "data_m4.pkl"),
    HF5_1K=("HF/HF5_1K.pkl", HF_URL_BASE + "data_m5.pkl"),
    HF6_1K=("HF/HF6_1K.pkl", HF_URL_BASE + "data_m6.pkl"),
    HF3_10K=("HF/HF3_10K.pkl", HF_URL_BASE + "data_m3_10k.pkl"),
    HF4_10K=("HF/HF4_10K.pkl", HF_URL_BASE + "data_m4_10k.pkl"),
    HF5_10K=("HF/HF5_10K.pkl", HF_URL_BASE + "data_m5_10k.pkl"),
    HF6_10K=("HF/HF6_10K.pkl", HF_URL_BASE + "data_m6_10k.pkl"),
    HX2=("HF/HX2.pkl", HF_URL_BASE + "data_HX2.pkl"),
    HX3=("HF/HX3.pkl", HF_URL_BASE + "data_HX3.pkl"),
    HX4=("HF/HX4.pkl", HF_URL_BASE + "data_HX4.pkl"),
    HX5=("HF/HX5.pkl", HF_URL_BASE + "data_HX5.pkl"),
    HX6=("HF/HX6.pkl", HF_URL_BASE + "data_HX6.pkl")
    )


#def https_open_with_auth(url, user, passwd):
#    request = urllib2.Request(url)
#    user_pass = base64.b64encode('{}:{}'.format(user, passwd))
#    request.add_header("Authorization", "Basic {}".format(user_pass))
#    return urllib2.urlopen(request)

def _get_or_download_dataset(dataset_name, path=None):
    rel_path, url = dataset_info[dataset_name]
    
    if path is None:
        paths = get_data_dirs()
    else:
        paths = [path]


