from torchvision.models import alexnet
from torchvision.models import vgg11
from torchvision.models import googlenet
from torchvision.models import resnet18

def get_pretrained_model(model_name: str, num_classes: int, pretrained: bool=True):
    if (model_name == "alexnet"):
        return alexnet(pretrained=pretrained, num_classes=num_classes)

    if (model_name == "vgg11"):
        return vgg11(pretrained=pretrained, num_classes=num_classes)

    if (model_name == "googlenet"):
        return googlenet(pretrained=pretrained, num_classes=num_classes)

    if (model_name == "resnet18"):
        return resnet18(pretrained=pretrained, num_classes=num_classes)