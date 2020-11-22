import sniff_network
import fill_form
import send_mail
import config
import time




if __name__ == '__main__':
    print(config.MAC_ADR)
    sent_mail = False
    while(not sent_mail):
        print("Starting..")
        if not sniff_network.sniff(config.MAC_ADR):
            fill_form.generer_attestation(config.PRENOM, config.NOM, config.DDN, config.LDN, config.ADDR, config.VILLE, config.CP)
            send_mail.send_mail(config.EMAIL, config.SUJET_MAIL, config.BODY_MAIL, config.PWD)
            time.sleep(2)
            send_mail.move_pdf_toarch()
            sent_mail = True
        else:
            print("no mac adress found !")
