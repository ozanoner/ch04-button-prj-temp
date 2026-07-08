
#include <esp_log.h>
#include <esp_err.h>
#include "iot_button.h"
#include "button_gpio.h"
#include "sdkconfig.h"

#define TAG "app"
#define APP_BUTTON_GPIO CONFIG_APP_BUTTON

static button_handle_t app_button = NULL;

static void app_single_click_cb(void *button_handle, void *usr_data)
{
    ESP_LOGI(TAG, "single-click");
}

static void app_long_press_cb(void *button_handle, void *usr_data)
{
    ESP_LOGI(TAG, "long-press");
}

void app_main(void)
{
    const button_config_t button_cfg = {0};

    const button_gpio_config_t gpio_cfg = {
        .gpio_num = APP_BUTTON_GPIO};

    ESP_LOGI(TAG, "button gpio num: %d", APP_BUTTON_GPIO);

    ESP_ERROR_CHECK(iot_button_new_gpio_device(&button_cfg, &gpio_cfg, &app_button));

    ESP_ERROR_CHECK(iot_button_register_cb(app_button, BUTTON_SINGLE_CLICK, NULL, app_single_click_cb, NULL));
    ESP_ERROR_CHECK(iot_button_register_cb(app_button, BUTTON_LONG_PRESS_START, NULL, app_long_press_cb, NULL));
}
