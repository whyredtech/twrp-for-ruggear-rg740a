$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/aosp_base.mk)
$(call inherit-product, vendor/twrp/config/common.mk)
PRODUCT_DEVICE := rg740a
PRODUCT_NAME := twrp_rg740a
PRODUCT_BRAND := Ruggear
PRODUCT_MODEL := RG740A
PRODUCT_MANUFACTURER := Ruggear
