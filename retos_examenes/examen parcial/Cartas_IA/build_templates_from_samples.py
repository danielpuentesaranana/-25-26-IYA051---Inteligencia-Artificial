import cv2
import numpy as np
import os

# Carpetas de entrada (recortes en color o gris)
SAMPLES_VALUES_DIR = "samples/values"
SAMPLES_SUITS_DIR  = "samples/suits"

# Carpetas de salida (plantillas listas para usar)
TEMPLATES_VALUES_DIR = "templates/values"
TEMPLATES_SUITS_DIR  = "templates/suits"

# Tamaño objetivo
VALUE_SIZE = (40, 60)  # width, height
SUIT_SIZE  = (40, 40)


def binarize_and_resize(path, size):
    """Carga, binariza (símbolo blanco sobre fondo negro) y redimensiona."""
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(path)

    blur = cv2.GaussianBlur(img, (3, 3), 0)

    # Símbolo blanco, fondo negro
    _, bin_img = cv2.threshold(
        blur, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    resized = cv2.resize(bin_img, size, interpolation=cv2.INTER_AREA)
    return resized


def process_folder(in_dir, out_dir, size):
    os.makedirs(out_dir, exist_ok=True)

    if not os.path.isdir(in_dir):
        print(f"[AVISO] Carpeta de entrada no existe: {in_dir}")
        return

    for fname in os.listdir(in_dir):
        if not fname.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        in_path = os.path.join(in_dir, fname)
        name, _ = os.path.splitext(fname)  

        try:
            tpl = binarize_and_resize(in_path, size)
        except FileNotFoundError:
            print(f"[ERROR] No se pudo leer {in_path}")
            continue

        out_path = os.path.join(out_dir, f"{name}.png")
        cv2.imwrite(out_path, tpl)
        print(f"[OK] {in_path} -> {out_path}")


def main():
    # Valores (números/letras)
    print("=== Generando plantillas de VALOR ===")
    process_folder(SAMPLES_VALUES_DIR, TEMPLATES_VALUES_DIR, VALUE_SIZE)

    # Palos
    print("\n=== Generando plantillas de PALO ===")
    process_folder(SAMPLES_SUITS_DIR, TEMPLATES_SUITS_DIR, SUIT_SIZE)

    print("\nListo. Plantillas generadas en 'templates/values' y 'templates/suits'.")


if __name__ == "__main__":
    main()
