from machine import Pin, PWM, RTC
import time
# ===== دیاریکردنی LED =====
try:
    led = Pin("LED", Pin.OUT)
except:
    led = Pin(25, Pin.OUT)
# ===== دیاریکردنی BUZZER لەسەر GP15 =====
buzzer = PWM(Pin(15))
buzzer.duty_u16(0)
# ===== دیاریکردنی RTC =====
rtc = RTC()

def tick_sound():
    """BUZZERدەنگی توت — کورت و بەرز"""
    buzzer.freq(2500)        # فرێکوێنسی بەرز بۆ "توت"
    buzzer.duty_u16(20000)   # کەمێک کەم بۆ دەنگی نەرم
    time.sleep_ms(15)        # زۆر کورت
    buzzer.duty_u16(0)

def tick_led():
    """LED بە خێرایی دەدرەوشێتەوە"""
    led.value(1)
    time.sleep_ms(15)
    led.value(0)

print(" کاتژمێر دەستیپێکرد")
last_second = -1

while True:
    now = rtc.datetime()
    current_second = now[6]   # چرکە
    # ئەگەر چرکەیەکی نوێ دەستیپێکرد
    if current_second != last_second:
        last_second = current_second
        # پیشاندانی کات و بەروار لە Shell
        print("📅 {:04d}-{:02d}-{:02d}  ⏰ {:02d}:{:02d}:{:02d}".format(
            now[0], now[1], now[2], now[4], now[5], now[6]
        ))
        # پرتە کردنی LED + دەنگی توت
        tick_led()
        tick_sound()
    time.sleep_ms(20)   # پشکنینی خێرا بۆ وردبینی
    