from asml_product_p4_complitho import process_window, wavelength_window

pol = process_window(
    {
        "na": 0.55,
        "pitch_nm": 40.0,
        "pol_degree": 0.9,
        "pol_angle_deg": 45.0,
        "dose": 1.0,
        "defocus": 0.0,
        "blur": 0.1,
    }
)
wav = wavelength_window(
    {
        "wavelength_nm": 6.7,
        "na": 0.55,
        "multilayer_R": 0.7,
        "resist_blur_nm": 2.0,
        "dose": 1.0,
        "k1_proxy": 0.5,
    }
)
print(pol.to_dict())
print(wav.to_dict())
