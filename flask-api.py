import io
from pickletools import read_uint1
from torchvision import models
import json
from flask import Flask, jsonify, request
from flask import make_response
import torchvision.transforms as transforms
import torch
from PIL import Image
import os