import torchvision.transforms as T

def get_augmentations(train: bool = True) -> T.Compose:
    if train:
        return T.Compose(
            [
                T.Resize((224,224)),
                T.RandomResizedCrop(size=32, scale=(0.8, 1.1)),
                T.RandomHorizontalFlip(p=0.5),
                T.RandomAdjustSharpness(sharpness_factor=2),
                T.ToTensor(),
                T.Normalize((0.49139968, 0.48215841, 0.44653091), (0.24703223, 0.24348513, 0.26158784))
            ]
        )
    else:
        return T.Compose(
            [
                T.Resize((224,224)),
                T.ToTensor(),
                T.Normalize((0.49139968, 0.48215841, 0.44653091), (0.24703223, 0.24348513, 0.26158784))
            ]
        )

