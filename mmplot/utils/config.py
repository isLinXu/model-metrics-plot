
from pathlib import Path
from typing import Dict, Union

from difflib import get_close_matches

from omegaconf import DictConfig, OmegaConf

from utils.logger import LOGGER, colorstr

# Constants
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]
DEFAULT_CONFIG = ROOT / "configs/default.yaml"


def check_config_mismatch(overrides, cfg):
    mismatched = [option for option in overrides if option not in cfg and 'hydra.' not in option]

    for option in mismatched:
        LOGGER.info(f"{colorstr(option)} is not a valid key. Similar keys: {get_close_matches(option, cfg, 3, 0.6)}")
    if mismatched:
        exit()

def get_config(config: Union[str, DictConfig], overrides: Union[str, Dict] = None):
    """
    Load and merge configuration data from a file or dictionary.

    Args:
        config (Union[str, DictConfig]): Configuration data in the form of a file name or a DictConfig object.
        overrides (Union[str, Dict], optional): Overrides in the form of a file name or a dictionary. Default is None.

    Returns:
        OmegaConf.Namespace: Training arguments namespace.
    """
    if overrides is None:
        overrides = {}
    if isinstance(config, (str, Path)):
        config = OmegaConf.load(config)
    elif isinstance(config, Dict):
        config = OmegaConf.create(config)
    # override
    if isinstance(overrides, str):
        overrides = OmegaConf.load(overrides)
    elif isinstance(overrides, Dict):
        overrides = OmegaConf.create(overrides)

    check_config_mismatch(dict(overrides).keys(), dict(config).keys())

    return OmegaConf.merge(config, overrides)