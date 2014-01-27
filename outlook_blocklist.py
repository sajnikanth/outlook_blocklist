from selenium import webdriver
import unittest
import getpass


class Outlook(unittest.TestCase):
    def test_outlook(self):
        email = raw_input("Enter your outlook email: ")
        password = getpass.getpass()
        driver = webdriver.Firefox()
        driver.get("http://outlook.com")
        driver.find_element_by_id("i0116").clear()
        driver.find_element_by_id("i0116").send_keys(email)
        driver.find_element_by_id("i0118").send_keys(password)
        driver.find_element_by_id("idSIButton9").click()
        if "https://blu176.mail.live.com/default.aspx" in driver.current_url:
            driver.get("https://blu176.mail.live.com/P.mvc#!/mail/options.aspx?subsection=8&n=1222346407")
            driver.switch_to_frame("appFrame")
            domains = ("1placenine3.com", "2very.com", "acecrm.in", "adcapitalobtain.com", "addressnegotiateoverhaul.com", "addresssynthesizedevelop.com", "adget.in", "administerupgradereserve.com", "admireadoreprepare.com", "advertisedetectapply.com", "agunclog.us", "airtel.in", "akainfohairreviews.com", "allbjurm.info", "americangiftsxmas.com", "amitydebut.com", "antrathin.com", "anydigitalservice.com", "arbitrateplaninterview.com", "arbitratesurveyfabricate.com", "arrangeexploreengineer.com", "azirid.us", "babysite.nl", "bestsavingspath.com", "bestsavingsportal.com", "bestsavingsscout.com", "bestsavingsusa.com", "bestsavingsweb.com", "bestsuperclick.com", "besttopshot.net", "bigdaybulletin.com", "bighitman.com", "birlasunlife.com", "bose.com", "bounce.linkedin.com", "bpomail.co.uk", "buzzbaron.com", "caphaf.us", "capitaland.com", "center4imedia.biz", "circulationmails.com", "clarifyinstitute.com", "clickheretops.net", "clickpresentstate.net", "clickquidetoday.net", "clicksiteworld.com", "clickusablesite.net", "clickvisitguide.com", "client1.emailsun.biz", "cmail3.com", "collaborateadaptresolve.com", "colorplusonline.com", "comcast.net", "communicatesearchdebug.com", "companyspeedcompany.com", "companystudiostreamline.com", "condenseoperateexecute.com", "constructmoderateappoint.com", "constructoverhaulremodel.com", "contactreviewconstruct.com", "contactsolicitateconsult.com", "contactspeakwrite.com", "contractdecidesupervise.com", "contractinspecthandle.com", "contractpremiuminspect.com", "contributedir.com", "controlcommercestrengthen.com", "controlexperteliminate.com", "controlfocusdirect.com", "controlhandleeliminate.com", "convinceextractprint.com", "cooltoptravel.com", "coordinationsenne.be", "creativedealz.com", "dalalstreetjournal.com", "dalalstreetmails.com", "dancebash.com", "dealbeatz.com", "dealfries.com", "dealfrnch.com", "dealmyntra.com", "debategathertexts.com", "december8deals.com", "dengesandalye.com", "developpurchaseexecute.com", "dientang.us", "digicare.co", "digicircuit.com", "digital-mailers.in", "dlcheckerz.com", "donedelz.com", "draftin.biz", "dsij.biz", "dsij.in", "easychoices.net", "edm.tigerair.com", "elitestatus.net", "em.compareraja.com", "em.couponraja.com", "emaarket.info", "email.microsoft.com", "exchange.1and1.com", "exportersmart.com", "fabricateprintstandardize.com", "facebookmail.com", "felicity-group.org", "felicity-maple.org", "fieldmediasearch.com", "fighern.info", "fixya.com", "fleetingimage.net", "flowerfleachamp.com", "flymailers.com", "freetravelship.com", "fullydesigned.net", "fundbazzar.info", "funkpunk.com", "gigabaron.com", "gigakeeper.com", "gigamogul.com", "gigamonger.com", "gkboptical.com", "godhuraus.info", "goodinvestmentguide.com", "greatsitesuper.com", "hinet.net", "hinfenush.us", "holidaydeals2u.com", "holidaygiftguidez.com", "home-fix.com", "icicibank.com", "indianacademy.net.in", "informstriking-90.com", "informwebsite.com", "infotopcreate.com", "initiatefavor.com", "initiateincrease.com", "initiaterestoreapprove.com", "intervar.com.ar", "ipaidabribe.com", "jhbaxter.com", "joinmeasurebuild.com", "judern.us", "justthewayitcouldbe.com", "kara80.com", "kat33.com", "kolkatarocks.com", "kwalithed.us", "libero.it", "linkmailers.com", "listenmeasurefortify.com", "maacmail.com", "mail.payback.in", "mail4gs.org", "mail63.us2.mcsv.net", "mailfb.in", "mailmantras.com", "matchdragon.com", "maximumsavingstoday.com", "mcchord.af.mil", "membercare.imintpoints.co.in", "miamisupersite.com", "moderatefabricate.com", "moneybazar.biz", "mtdigital.in", "mysavercentral.com", "mysavernow.com", "mysuperstories.com", "nextstep4itmail.com", "notify-express.com", "objecttorrent.com", "officeliveemail.com", "olagarmy.com", "onlinesavingspath.com", "onlinesavingsscout.com", "ordertoprint.in", "orpack.us", "outlineconductconstruct.com", "paceroom.net", "peoplelovethese.com", "postmastermails.com", "promotehere.net", "quickestway.net", "repairstudyapply.com", "reply.digitalriver.com", "reserved-message.com", "ruddly.us", "safeonlineshopp.com", "safetoclicknow.com", "samplesales4u.com", "searchover.net", "seemspossible.com", "selfrely.net", "sendcheapsuper.com", "senddoubleclick.com", "sendvisitguide.com", "service.weibo.com", "sgsend.com", "shaltsteed.com", "shinejobz.com", "shoppingtime.info", "shreestructure.in", "simplifiedmails.com", "singmailing.com", "smartmail4u.org", "smcinsurance.biz", "smude.edu.in", "solicitatelocaterepair.com", "somethang4everyone.com", "sopris.net", "space.sina.com.cn", "sprsaver.com", "squiggly.com", "stmate.us", "supertradesite.com", "supertravelsite.com", "sweetdlz.com", "talktalk.net", "tfsbistrot.ccsend.com", "theclicksearch.com", "thefaxbulletin.com", "tipofftraders.com", "tiscali.co.uk", "tns-online.com", "transmittravel.com", "adaptroutesearch.com", "losocongo.us", "incorporateoutlinearbitrate.com", "combineoperategather.com", "liftedspirits.net", "universalsolutionsnow.com", "giventime.net", "bestsavingscentral.com", "convincereferwritetestsway.com", "notice-account.com", "thesendflowers.com", "draftprocessrecord.com", "hiddenvalue.net", "sharedideas.net", "avtlg.ru", "cipi-magie.com", "mailpro.co.in", "maebag.info", "composefileorder.com", "mms.viacommedianetworks.com")
            for i in range(0, len(domains)):
                driver.implicitly_wait(1)
                driver.find_element_by_id("ctl05_TextToAdd").send_keys(domains[i])
                driver.find_element_by_id("ctl05_Add").click()
        else:
            print "User not logged in"
        driver.quit()
if __name__ == "__main__":
    unittest.main()
