import datetime as dt
import matplotlib
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Set the title of the Streamlit app
st.title('Correlation Heatmap Generator')
st.write('by anikxtsingh')

st.subheader('ReadMe')
st.write('Explore the correlations between stocks with our interactive heatmap generator. Correlation measures the relationship between two or more variables, such as stock prices.\n\n A correlation close to +1 indicates a strong positive relationship, meaning the stocks tend to move in the same direction. A correlation close to -1 indicates a strong negative relationship, meaning the stocks move in opposite directions.\n\n Understanding these correlations can help in diversifying portfolios and managing risk effectively. Choose from a wide range of stocks and indices, including NSE and major US companies, and uncover insights with just a few clicks.')

# User input for start and end dates
end_date = dt.date.today()
start_date = dt.date(end_date.year-1, end_date.month, end_date.day)

from_date = st.date_input('Start Date', start_date)
to_date = st.date_input('End Date', end_date)


# User input for selecting tickers


default_tickers = [ '^GSPC','^NSEI', '^BSESN','20MICRONS.NS',
'21STCENMGM.NS',
'3IINFOTECH.NS',
'3MINDIA.NS',
'3PLAND.NS',
'5PAISA.NS',
'63MOONS.NS',
'8KMILES.NS',
'A2ZINFRA.NS',
'AAKASH.NS',
'AARON.NS',
'AARTIDRUGS.NS',
'AARTIIND.NS',
'AARTISURF.NS',
'AARVEEDEN.NS',
'AARVI.NS',
'AAVAS.NS',
'ABAN.NS',
'ABB.NS',
'ABBOTINDIA.NS',
'ABCAPITAL.NS',
'ABFRL.NS',
'ABMINTLTD.NS',
'ACC.NS',
'ACCELYA.NS',
'ACCURACY.NS',
'ACE.NS',
'ACRYSIL.NS',
'ADANIENT.NS',
'ADANIGREEN.NS',
'ADANIPORTS.NS',
'ADANIPOWER.NS',
'ADANITRANS.NS',
'ADFFOODS.NS',
'ADHUNIKIND.NS',
'ADL.NS',
'ADORWELD.NS',
'ADROITINFO.NS',
'ADSL.NS',
'ADVANIHOTR.NS',
'ADVENZYMES.NS',
'AEGISCHEM.NS',
'AFFLE.NS',
'AGARIND.NS',
'AGCNET.NS',
'AGRITECH.NS',
'AGROPHOS.NS',
'AHLEAST.NS',
'AHLUCONT.NS',
'AHLWEST.NS',
'AIAENG.NS',
'AIRAN.NS',
'AJANTPHARM.NS',
'AJMERA.NS',
'AKASH.NS',
'AKSHARCHEM.NS',
'AKSHOPTFBR.NS',
'AKZOINDIA.NS',
'ALANKIT.NS',
'ALBERTDAVD.NS',
'ALCHEM.NS',
'ALEMBICLTD.NS',
'ALICON.NS',
'ALKALI.NS',
'ALKEM.NS',
'ALKYLAMINE.NS',
'ALLCARGO.NS',
'ALLSEC.NS',
'ALMONDZ.NS',
'ALOKINDS.NS',
'ALPA.NS',
'ALPHAGEO.NS',
'ALPSINDUS.NS',
'AMARAJABAT.NS',
'AMBER.NS',
'AMBIKCO.NS',
'AMBUJACEM.NS',
'AMDIND.NS',
'AMJLAND.NS',
'AMRUTANJAN.NS',
'ANANTRAJ.NS',
'ANDHRACEMT.NS',
'ANDHRAPAP.NS',
'ANDHRSUGAR.NS',
'ANGELBRKG.NS',
'ANIKINDS.NS',
'ANKITMETAL.NS',
'ANSALAPI.NS',
'ANSALHSG.NS',
'ANUP.NS',
'APARINDS.NS',
'APCL.NS',
'APCOTEXIND.NS',
'APEX.NS',
'APLAPOLLO.NS',
'APLLTD.NS',
'APOLLO.NS',
'APOLLOHOSP.NS',
'APOLLOPIPE.NS',
'APOLLOTYRE.NS',
'APOLSINHOT.NS',
'APTECHT.NS',
'ARCHIDPLY.NS',
'ARCHIES.NS',
'ARCOTECH.NS',
'ARENTERP.NS',
'ARIES.NS',
'ARIHANT.NS',
'ARIHANTSUP.NS',
'ARMANFIN.NS',
'AROGRANITE.NS',
'ARROWGREEN.NS',
'ARSHIYA.NS',
'ARSSINFRA.NS',
'ARTEMISMED.NS',
'ARVIND.NS',
'ARVINDFASN.NS',
'ARVSMART.NS',
'ASAHIINDIA.NS',
'ASAHISONG.NS',
'ASAL.NS',
'ASALCBR.NS',
'ASHAPURMIN.NS',
'ASHIANA.NS',
'ASHIMASYN.NS',
'ASHOKA.NS',
'ASHOKLEY.NS',
'ASIANHOTNR.NS',
'ASIANPAINT.NS',
'ASIANTILES.NS',
'ASPINWALL.NS',
'ASTEC.NS',
'ASTERDM.NS',
'ASTRAL.NS',
'ASTRAMICRO.NS',
'ASTRAZEN.NS',
'ASTRON.NS',
'ATFL.NS',
'ATGL.NS',
'ATLANTA.NS',
'ATLASCYCLE.NS',
'ATUL.NS',
'ATULAUTO.NS',
'AUBANK.NS',
'AURIONPRO.NS',
'AUROPHARMA.NS',
'AUSOMENT.NS',
'AUTOAXLES.NS',
'AUTOIND.NS',
'AUTOLITIND.NS',
'AVADHSUGAR.NS',
'AVANTIFEED.NS',
'AVTNPL.NS',
'AWHCL.NS',
'AXISBANK.NS',
'AXISCADES.NS',
'AYMSYNTEX.NS',
'BAFNAPH.NS',
'BAGFILMS.NS',
'BAJAJ-AUTO.NS',
'BAJAJCON.NS',
'BAJAJELEC.NS',
'BAJAJFINSV.NS',
'BAJAJHIND.NS',
'BAJAJHLDNG.NS',
'BAJFINANCE.NS',
'BALAJITELE.NS',
'BALAMINES.NS',
'BALAXI.NS',
'BALKRISHNA.NS',
'BALKRISIND.NS',
'BALLARPUR.NS',
'BALMLAWRIE.NS',
'BALPHARMA.NS',
'BALRAMCHIN.NS',
'BANARBEADS.NS',
'BANARISUG.NS',
'BANCOINDIA.NS',
'BANDHANBNK.NS',
'BANG.NS',
'BANKA.NS',
'BANKBARODA.NS',
'BANKINDIA.NS',
'BANSWRAS.NS',
'BARTRONICS.NS',
'BASF.NS',
'BASML.NS',
'BATAINDIA.NS',
'BAYERCROP.NS',
'BBL.NS',
'BBTC.NS',
'BCG.NS',
'BCP.NS',
'BDL.NS',
'BEARDSELL.NS',
'BECTORFOOD.NS',
'BEDMUTHA.NS',
'BEL.NS',
'BEML.NS',
'BEPL.NS',
'BERGEPAINT.NS',
'BFINVEST.NS',
'BFUTILITIE.NS',
'BGRENERGY.NS',
'BHAGERIA.NS',
'BHAGYANGR.NS',
'BHAGYAPROP.NS',
'BHANDARI.NS',
'BHARATFORG.NS',
'BHARATGEAR.NS',
'BHARATRAS.NS',
'BHARATWIRE.NS',
'BHARTIARTL.NS',
'BHEL.NS',
'BIGBLOC.NS',
'BIL.NS',
'BILENERGY.NS',
'BINDALAGRO.NS',
'BIOCON.NS',
'BIOFILCHEM.NS',
'BIRLACABLE.NS',
'BIRLACORPN.NS',
'BIRLAMONEY.NS',
'BIRLATYRE.NS',
'BKMINDST.NS',
'BLBLIMITED.NS',
'BLISSGVS.NS',
'BLKASHYAP.NS',
'BLS.NS',
'BLUECOAST.NS',
'BLUEDART.NS',
'BLUESTARCO.NS',
'BODALCHEM.NS',
'BOMDYEING.NS',
'BOROLTD.NS',
'BORORENEW.NS',
'BOSCHLTD.NS',
'BPCL.NS',
'BPL.NS',
'BRFL.NS',
'BRIGADE.NS',
'BRITANNIA.NS',
'BRNL.NS',
'BROOKS.NS',
'BSE.NS',
'BSELINFRA.NS',
'BSHSL.NS',
'BSL.NS',
'BSOFT.NS',
'BURGERKING.NS',
'BURNPUR.NS',
'BUTTERFLY.NS',
'BVCL.NS',
'BYKE.NS',
'CADILAHC.NS',
'CALSOFT.NS',
'CAMLINFINE.NS',
'CAMS.NS',
'CANBK.NS',
'CANDC.NS',
'CANFINHOME.NS',
'CANTABIL.NS',
'CAPACITE.NS',
'CAPLIPOINT.NS',
'CAPTRUST.NS',
'CARBORUNIV.NS',
'CAREERP.NS',
'CARERATING.NS',
'CASTROLIND.NS',
'CCHHL.NS',
'CCL.NS',
'CDSL.NS',
'CEATLTD.NS',
'CEBBCO.NS',
'CELEBRITY.NS',
'CENTENKA.NS',
'CENTEXT.NS',
'CENTRALBK.NS',
'CENTRUM.NS',
'CENTUM.NS',
'CENTURYPLY.NS',
'CENTURYTEX.NS',
'CERA.NS',
'CEREBRAINT.NS',
'CESC.NS',
'CESCVENT.NS',
'CGCL.NS',
'CGPOWER.NS',
'CHALET.NS',
'CHAMBLFERT.NS',
'CHEMBOND.NS',
'CHEMCON.NS',
'CHEMFAB.NS',
'CHENNPETRO.NS',
'CHOLAFIN.NS',
'CHOLAHLDNG.NS',
'CHROMATIC.NS',
'CIGNITITEC.NS',
'CINELINE.NS',
'CINEVISTA.NS',
'CIPLA.NS',
'CLEDUCATE.NS',
'CLNINDIA.NS',
'CMICABLES.NS',
'CNOVAPETRO.NS',
'COALINDIA.NS',
'COCHINSHIP.NS',
'COFORGE.NS',
'COLPAL.NS',
'COMPINFO.NS',
'COMPUSOFT.NS',
'CONCOR.NS',
'CONFIPET.NS',
'CONSOFINVT.NS',
'CONTROLPR.NS',
'CORALFINAC.NS',
'CORDSCABLE.NS',
'COROMANDEL.NS',
'COSMOFILMS.NS',
'COUNCODOS.NS',
'COX&KINGS.NS',
'CREATIVE.NS',
'CREATIVEYE.NS',
'CREDITACC.NS',
'CREST.NS',
'CRISIL.NS',
'CROMPTON.NS',
'CSBBANK.NS',
'CTE.NS',
'CUB.NS',
'CUBEXTUB.NS',
'CUMMINSIND.NS',
'CUPID.NS',
'CYBERMEDIA.NS',
'CYBERTECH.NS',
'CYIENT.NS',
'DAAWAT.NS',
'DABUR.NS',
'DALBHARAT.NS',
'DALMIASUG.NS',
'DAMODARIND.NS',
'DANGEE.NS',
'DATAMATICS.NS',
'DBCORP.NS',
'DBL.NS',
'DBREALTY.NS',
'DBSTOCKBRO.NS',
'DCAL.NS',
'DCBBANK.NS',
'DCM.NS',
'DCMFINSERV.NS',
'DCMNVL.NS',
'DCMSHRIRAM.NS',
'DCW.NS',
'DECCANCE.NS',
'DEEPAKFERT.NS',
'DEEPAKNTR.NS',
'DEEPENR.NS',
'DELTACORP.NS',
'DELTAMAGNT.NS',
'DEN.NS',
'DENORA.NS',
'DFMFOODS.NS',
'DGCONTENT.NS',
'DHAMPURSUG.NS',
'DHANBANK.NS',
'DHANI.NS',
'DHANUKA.NS',
'DHARSUGAR.NS',
'DHFL.NS',
'DHUNINV.NS',
'DIAMONDYD.NS',
'DIAPOWER.NS',
'DICIND.NS',
'DIGISPICE.NS',
'DIGJAMLTD.NS',
'DISHTV.NS',
'DIVISLAB.NS',
'DIXON.NS',
'DLF.NS',
'DLINKINDIA.NS',
'DMART.NS',
'DNAMEDIA.NS',
'DOLAT.NS',
'DOLLAR.NS',
'DONEAR.NS',
'DPABHUSHAN.NS',
'DPSCLTD.NS',
'DPWIRES.NS',
'DQE.NS',
'DREDGECORP.NS',
'DRREDDY.NS',
'DSSL.NS',
'DTIL.NS',
'DUCON.NS',
'DVL.NS',
'DWARKESH.NS',
'DYNAMATECH.NS',
'DYNPRO.NS',
'EASTSILK.NS',
'EASUNREYRL.NS',
'EBIXFOREX.NS',
'ECLERX.NS',
'EDELWEISS.NS',
'EDUCOMP.NS',
'EICHERMOT.NS',
'EIDPARRY.NS',
'EIHAHOTELS.NS',
'EIHOTEL.NS',
'EIMCOELECO.NS',
'EKC.NS',
'ELECON.NS',
'ELECTCAST.NS',
'ELECTHERM.NS',
'ELGIEQUIP.NS',
'ELGIRUBCO.NS',
'EMAMILTD.NS',
'EMAMIPAP.NS',
'EMAMIREAL.NS',
'EMCO.NS',
'EMKAY.NS',
'EMMBI.NS',
'ENDURANCE.NS',
'ENERGYDEV.NS',
'ENGINERSIN.NS',
'ENIL.NS',
'EPL.NS',
'EQUITAS.NS',
'EQUITASBNK.NS',
'ERIS.NS',
'EROSMEDIA.NS',
'ESABINDIA.NS',
'ESCORTS.NS',
'ESSARSHPNG.NS',
'ESTER.NS',
'EUROMULTI.NS',
'EUROTEXIND.NS',
'EVEREADY.NS',
'EVERESTIND.NS',
'EXCEL.NS',
'EXCELINDUS.NS',
'EXIDEIND.NS',
'EXPLEOSOL.NS',
'FACT.NS',
'FAIRCHEMOR.NS',
'FCL.NS',
'FCONSUMER.NS',
'FCSSOFT.NS',
'FDC.NS',
'FEDERALBNK.NS',
'FEL.NS',
'FELDVR.NS',
'FIEMIND.NS',
'FILATEX.NS',
'FINCABLES.NS',
'FINEORG.NS',
'FINPIPE.NS',
'FLEXITUFF.NS',
'FLFL.NS',
'FLUOROCHEM.NS',
'FMGOETZE.NS',
'FMNL.NS',
'FORCEMOT.NS',
'FORTIS.NS',
'FOSECOIND.NS',
'FRETAIL.NS',
'FSC.NS',
'FSL.NS',
'GABRIEL.NS',
'GAEL.NS',
'GAIL.NS',
'GAL.NS',
'GALAXYSURF.NS',
'GALLANTT.NS',
'GALLISPAT.NS',
'GAMMNINFRA.NS',
'GANDHITUBE.NS',
'GANECOS.NS',
'GANESHHOUC.NS',
'GANGESSECU.NS',
'GARDENSILK.NS',
'GARFIBRES.NS',
'GATI.NS',
'GAYAHWS.NS',
'GAYAPROJ.NS',
'GBGLOBAL.NS',
'GDL.NS',
'GEECEE.NS',
'GEEKAYWIRE.NS',
'GENESYS.NS',
'GENUSPAPER.NS',
'GENUSPOWER.NS',
'GEOJITFSL.NS',
'GEPIL.NS',
'GESHIP.NS',
'GET&D.NS',
'GFLLIMITED.NS',
'GFSTEELS.NS',
'GHCL.NS',
'GICHSGFIN.NS',
'GICRE.NS',
'GILLANDERS.NS',
'GILLETTE.NS',
'GINNIFILA.NS',
'GIPCL.NS',
'GISOLUTION.NS',
'GKWLIMITED.NS',
'GLAND.NS',
'GLAXO.NS',
'GLENMARK.NS',
'GLFL.NS',
'GLOBAL.NS',
'GLOBALVECT.NS',
'GLOBE.NS',
'GLOBOFFS.NS',
'GLOBUSSPR.NS',
'GMBREW.NS',
'GMDCLTD.NS',
'GMMPFAUDLR.NS',
'GMRINFRA.NS',
'GNA.NS',
'GNFC.NS',
'GOACARBON.NS',
'GOCLCORP.NS',
'GODFRYPHLP.NS',
'GODHA.NS',
'GODREJAGRO.NS',
'GODREJCP.NS',
'GODREJIND.NS',
'GODREJPROP.NS',
'GOENKA.NS',
'GOKEX.NS',
'GOKUL.NS',
'GOKULAGRO.NS',
'GOLDENTOBC.NS',
'GOLDIAM.NS',
'GOLDTECH.NS',
'GOODLUCK.NS',
'GOODYEAR.NS',
'GPIL.NS',
'GPPL.NS',
'GPTINFRA.NS',
'GRANULES.NS',
'GRAPHITE.NS',
'GRASIM.NS',
'GRAVITA.NS',
'GREAVESCOT.NS',
'GREENLAM.NS',
'GREENPANEL.NS',
'GREENPLY.NS',
'GREENPOWER.NS',
'GRINDWELL.NS',
'GROBTEA.NS',
'GRPLTD.NS',
'GRSE.NS',
'GSCLCEMENT.NS',
'GSFC.NS',
'GSPL.NS',
'GSS.NS',
'GTL.NS',
'GTLINFRA.NS',
'GTNIND.NS',
'GTNTEX.NS',
'GTPL.NS',
'GUFICBIO.NS',
'GUJALKALI.NS',
'GUJAPOLLO.NS',
'GUJGASLTD.NS',
'GUJRAFFIA.NS',
'GULFOILLUB.NS',
'GULFPETRO.NS',
'GULPOLY.NS',
'GVKPIL.NS',
'HAL.NS',
'HAPPSTMNDS.NS',
'HARITASEAT.NS',
'HARRMALAYA.NS',
'HATHWAY.NS',
'HATSUN.NS',
'HAVELLS.NS',
'HAVISHA.NS',
'HBLPOWER.NS',
'HBSL.NS',
'HCC.NS',
'HCG.NS',
'HCL-INSYS.NS',
'HCLTECH.NS',
'HDFC.NS',
'HDFCAMC.NS',
'HDFCBANK.NS',
'HDFCLIFE.NS',
'HDIL.NS',
'HEG.NS',
'HEIDELBERG.NS',
'HEMIPROP.NS',
'HERCULES.NS',
'HERITGFOOD.NS',
'HEROMOTOCO.NS',
'HESTERBIO.NS',
'HEXATRADEX.NS',
'HFCL.NS',
'HGINFRA.NS',
'HGS.NS',
'HIKAL.NS',
'HIL.NS',
'HILTON.NS',
'HIMATSEIDE.NS',
'HINDALCO.NS',
'HINDCOMPOS.NS',
'HINDCOPPER.NS',
'HINDMOTORS.NS',
'HINDNATGLS.NS',
'HINDOILEXP.NS',
'HINDPETRO.NS',
'HINDUNILVR.NS',
'HINDZINC.NS',
'HIRECT.NS',
'HISARMETAL.NS',
'HITECH.NS',
'HITECHCORP.NS',
'HITECHGEAR.NS',
'HLVLTD.NS',
'HMT.NS',
'HMVL.NS',
'HNDFDS.NS',
'HONAUT.NS',
'HONDAPOWER.NS',
'HOTELRUGBY.NS',
'HOVS.NS',
'HPL.NS',
'HSCL.NS',
'HSIL.NS',
'HTMEDIA.NS',
'HUBTOWN.NS',
'HUDCO.NS',
'HUHTAMAKI.NS',
'IBREALEST.NS',
'IBULHSGFIN.NS',
'ICEMAKE.NS',
'ICICIBANK.NS',
'ICICIGI.NS',
'ICICIPRULI.NS',
'ICIL.NS',
'ICRA.NS',
'IDBI.NS',
'IDEA.NS',
'IDFC.NS',
'IDFCFIRSTB.NS',
'IEX.NS',
'IFBAGRO.NS',
'IFBIND.NS',
'IFCI.NS',
'IFGLEXPOR.NS',
'IGARASHI.NS',
'IGL.NS',
'IGPL.NS',
'IIFL.NS',
'IIFLSEC.NS',
'IIFLWAM.NS',
'IITL.NS',
'IL&FSENGG.NS',
'IL&FSTRANS.NS',
'IMAGICAA.NS',
'IMFA.NS',
'IMPAL.NS',
'INDBANK.NS',
'INDHOTEL.NS',
'INDIACEM.NS',
'INDIAGLYCO.NS',
'INDIAMART.NS',
'INDIANB.NS',
'INDIANCARD.NS',
'INDIANHUME.NS',
'INDIGO.NS',
'INDLMETER.NS',
'INDNIPPON.NS',
'INDOCO.NS',
'INDORAMA.NS',
'INDOSOLAR.NS',
'INDOSTAR.NS',
'INDOTECH.NS',
'INDOTHAI.NS',
'INDOWIND.NS',
'INDRAMEDCO.NS',
'INDSWFTLAB.NS',
'INDSWFTLTD.NS',
'INDTERRAIN.NS',
'INDUSINDBK.NS',
'INDUSTOWER.NS',
'INEOSSTYRO.NS',
'INFIBEAM.NS',
'INFOBEAN.NS',
'INFOMEDIA.NS',
'INFY.NS',
'INGERRAND.NS',
'INOXLEISUR.NS',
'INOXWIND.NS',
'INSECTICID.NS',
'INSPIRISYS.NS',
'INTEGRA.NS',
'INTELLECT.NS',
'INTENTECH.NS',
'INVENTURE.NS',
'IOB.NS',
'IOC.NS',
'IOLCP.NS',
'IPCALAB.NS',
'IRB.NS',
'IRCON.NS',
'IRCTC.NS',
'ISEC.NS',
'ISFT.NS',
'ISMTLTD.NS',
'ITC.NS',
'ITDC.NS',
'ITDCEM.NS',
'ITI.NS',
'IVC.NS',
'IVP.NS',
'IZMO.NS',
'J&KBANK.NS',
'JAGRAN.NS',
'JAGSNPHARM.NS',
'JAIBALAJI.NS',
'JAICORPLTD.NS',
'JAIHINDPRO.NS',
'JAINSTUDIO.NS',
'JAMNAAUTO.NS',
'JASH.NS',
'JAYAGROGN.NS',
'JAYBARMARU.NS',
'JAYNECOIND.NS',
'JAYSREETEA.NS',
'JBCHEPHARM.NS',
'JBFIND.NS',
'JBMA.NS',
'JCHAC.NS',
'JETAIRWAYS.NS',
'JHS.NS',
'JINDALPHOT.NS',
'JINDALPOLY.NS',
'JINDALSAW.NS',
'JINDALSTEL.NS',
'JINDRILL.NS',
'JINDWORLD.NS',
'JISLDVREQS.NS',
'JISLJALEQS.NS',
'JITFINFRA.NS',
'JIYAECO.NS',
'JKCEMENT.NS',
'JKIL.NS',
'JKLAKSHMI.NS',
'JKPAPER.NS',
'JKTYRE.NS',
'JMA.NS',
'JMCPROJECT.NS',
'JMFINANCIL.NS',
'JMTAUTOLTD.NS',
'JOCIL.NS',
'JPASSOCIAT.NS',
'JPINFRATEC.NS',
'JPOLYINVST.NS',
'JPPOWER.NS',
'JSL.NS',
'JSLHISAR.NS',
'JSWENERGY.NS',
'JSWHL.NS',
'JSWISPL.NS',
'JSWSTEEL.NS',
'JTEKTINDIA.NS',
'JUBILANT.NS',
'JUBLFOOD.NS',
'JUBLINDS.NS',
'JUMPNET.NS',
'JUSTDIAL.NS',
'JYOTHYLAB.NS',
'JYOTISTRUC.NS',
'KABRAEXTRU.NS',
'KAJARIACER.NS',
'KAKATCEM.NS',
'KALPATPOWR.NS',
'KALYANI.NS',
'KALYANIFRG.NS',
'KAMATHOTEL.NS',
'KAMDHENU.NS',
'KANANIIND.NS',
'KANORICHEM.NS',
'KANPRPLA.NS',
'KANSAINER.NS',
'KAPSTON.NS',
'KARDA.NS',
'KARMAENG.NS',
'KARURVYSYA.NS',
'KAUSHALYA.NS',
'KAYA.NS',
'KCP.NS',
'KCPSUGIND.NS',
'KDDL.NS',
'KEC.NS',
'KECL.NS',
'KEERTI.NS',
'KEI.NS',
'KELLTONTEC.NS',
'KENNAMET.NS',
'KERNEX.NS',
'KESORAMIND.NS',
'KEYFINSERV.NS',
'KGL.NS',
'KHADIM.NS',
'KHAICHEM.NS',
'KHANDSE.NS',
'KICL.NS',
'KILITCH.NS',
'KINGFA.NS',
'KIOCL.NS',
'KIRIINDUS.NS',
'KIRLFER.NS',
'KIRLOSBROS.NS',
'KIRLOSENG.NS',
'KIRLOSIND.NS',
'KITEX.NS',
'KKCL.NS',
'KMSUGAR.NS',
'KNRCON.NS',
'KOKUYOCMLN.NS',
'KOLTEPATIL.NS',
'KOPRAN.NS',
'KOTAKBANK.NS',
'KOTARISUG.NS',
'KOTHARIPET.NS',
'KOTHARIPRO.NS',
'KPITTECH.NS',
'KPRMILL.NS',
'KRBL.NS',
'KREBSBIO.NS',
'KRIDHANINF.NS',
'KRISHANA.NS',
'KSB.NS',
'KSCL.NS',
'KSK.NS',
'KSL.NS',
'KTKBANK.NS',
'KUANTUM.NS',
'KWALITY.NS',
'L&TFH.NS',
'LAKPRE.NS',
'LALPATHLAB.NS',
'LAMBODHARA.NS',
'LAOPALA.NS',
'LASA.NS',
'LAURUSLABS.NS',
'LAXMIMACH.NS',
'LEMONTREE.NS',
'LFIC.NS',
'LGBBROSLTD.NS',
'LGBFORGE.NS',
'LIBAS.NS',
'LIBERTSHOE.NS',
'LICHSGFIN.NS',
'LIKHITHA.NS',
'LINCOLN.NS',
'LINCPEN.NS',
'LINDEINDIA.NS',
'LOKESHMACH.NS',
'LOTUSEYE.NS',
'LOVABLE.NS',
'LPDC.NS',
'LSIL.NS',
'LT.NS',
'LTI.NS',
'LTTS.NS',
'LUMAXIND.NS',
'LUMAXTECH.NS',
'LUPIN.NS',
'LUXIND.NS',
'LYKALABS.NS',
'LYPSAGEMS.NS',
'M&M.NS',
'M&MFIN.NS',
'MAANALU.NS',
'MACPOWER.NS',
'MADHAV.NS',
'MADHUCON.NS',
'MADRASFERT.NS',
'MAGADSUGAR.NS',
'MAGMA.NS',
'MAGNUM.NS',
'MAHABANK.NS',
'MAHAPEXLTD.NS',
'MAHASTEEL.NS',
'MAHEPC.NS',
'MAHESHWARI.NS',
'MAHINDCIE.NS',
'MAHLIFE.NS',
'MAHLOG.NS',
'MAHSCOOTER.NS',
'MAHSEAMLES.NS',
'MAITHANALL.NS',
'MAJESCO.NS',
'MALUPAPER.NS',
'MANAKALUCO.NS',
'MANAKCOAT.NS',
'MANAKSIA.NS',
'MANAKSTEEL.NS',
'MANALIPETC.NS',
'MANAPPURAM.NS',
'MANGALAM.NS',
'MANGCHEFER.NS',
'MANGLMCEM.NS',
'MANGTIMBER.NS',
'MANINDS.NS',
'MANINFRA.NS',
'MANUGRAPH.NS',
'MARALOVER.NS',
'MARATHON.NS',
'MARICO.NS',
'MARINE.NS',
'MARKSANS.NS',
'MARUTI.NS',
'MASFIN.NS',
'MASKINVEST.NS',
'MASTEK.NS',
'MATRIMONY.NS',
'MAWANASUG.NS',
'MAXHEALTH.NS',
'MAXIND.NS',
'MAXVIL.NS',
'MAYURUNIQ.NS',
'MAZDA.NS',
'MAZDOCK.NS',
'MBAPL.NS',
'MBECL.NS',
'MBLINFRA.NS',
'MCDHOLDING.NS',
'MCDOWELL-N.NS',
'MCL.NS',
'MCLEODRUSS.NS',
'MCX.NS',
'MEGASOFT.NS',
'MEGH.NS',
'MELSTAR.NS',
'MENONBE.NS',
'MEP.NS',
'MERCATOR.NS',
'METALFORGE.NS',
'METKORE.NS',
'METROPOLIS.NS',
'MFSL.NS',
'MGEL.NS',
'MGL.NS',
'MHRIL.NS',
'MIC.NS',
'MIDHANI.NS',
'MINDACORP.NS',
'MINDAIND.NS',
'MINDTECK.NS',
'MINDTREE.NS',
'MIRCELECTR.NS',
'MIRZAINT.NS',
'MITTAL.NS',
'MMFL.NS',
'MMP.NS',
'MMTC.NS',
'MODIRUBBER.NS',
'MOHITIND.NS',
'MOHOTAIND.NS',
'MOIL.NS',
'MOLDTECH.NS',
'MOLDTKPAC.NS',
'MONTECARLO.NS',
'MORARJEE.NS',
'MOREPENLAB.NS',
'MOTHERSUMI.NS',
'MOTILALOFS.NS',
'MOTOGENFIN.NS',
'MPHASIS.NS',
'MPSLTD.NS',
'MRF.NS',
'MRO-TEK.NS',
'MRPL.NS',
'MSPL.NS',
'MSTCLTD.NS',
'MTEDUCARE.NS',
'MTNL.NS',
'MUKANDENGG.NS',
'MUKANDLTD.NS',
'MUKTAARTS.NS',
'MUNJALAU.NS',
'MUNJALSHOW.NS',
'MURUDCERA.NS',
'MUTHOOTCAP.NS',
'MUTHOOTFIN.NS',
'NACLIND.NS',
'NAGAFERT.NS',
'NAGREEKCAP.NS',
'NAGREEKEXP.NS',
'NAHARCAP.NS',
'NAHARINDUS.NS',
'NAHARPOLY.NS',
'NAHARSPING.NS',
'NAM-INDIA.NS',
'NATCOPHARM.NS',
'NATHBIOGEN.NS',
'NATIONALUM.NS',
'NATNLSTEEL.NS',
'NAUKRI.NS',
'NAVINFLUOR.NS',
'NAVKARCORP.NS',
'NAVNETEDUL.NS',
'NBCC.NS',
'NBIFIN.NS',
'NBVENTURES.NS',
'NCC.NS',
'NCLIND.NS',
'NDGL.NS',
'NDL.NS',
'NDRAUTO.NS',
'NDTV.NS',
'NECCLTD.NS',
'NECLIFE.NS',
'NELCAST.NS',
'NELCO.NS',
'NEOGEN.NS',
'NESCO.NS',
'NESTLEIND.NS',
'NETWORK18.NS',
'NEULANDLAB.NS',
'NEWGEN.NS',
'NEXTMEDIA.NS',
'NFL.NS',
'NH.NS',
'NHPC.NS',
'NIACL.NS',
'NIITLTD.NS',
'NILAINFRA.NS',
'NILASPACES.NS',
'NILKAMAL.NS',
'NIPPOBATRY.NS',
'NIRAJ.NS',
'NIRAJISPAT.NS',
'NITCO.NS',
'NITINFIRE.NS',
'NITINSPIN.NS',
'NKIND.NS',
'NLCINDIA.NS',
'NMDC.NS',
'NOCIL.NS',
'NOIDATOLL.NS',
'NORBTEAEXP.NS',
'NOVARTIND.NS',
'NRAIL.NS',
'NRBBEARING.NS',
'NSIL.NS',
'NTL.NS',
'NTPC.NS',
'NUCLEUS.NS',
'NXTDIGITAL.NS',
'OAL.NS',
'OBEROIRLTY.NS',
'OCCL.NS',
'OFSS.NS',
'OIL.NS',
'OISL.NS',
'OLECTRA.NS',
'OMAXAUTO.NS',
'OMAXE.NS',
'OMMETALS.NS',
'ONELIFECAP.NS',
'ONEPOINT.NS',
'ONGC.NS',
'ONMOBILE.NS',
'ONWARDTEC.NS',
'OPTIEMUS.NS',
'OPTOCIRCUI.NS',
'ORBTEXP.NS',
'ORCHPHARMA.NS',
'ORICONENT.NS',
'ORIENTABRA.NS',
'ORIENTALTL.NS',
'ORIENTBELL.NS',
'ORIENTCEM.NS',
'ORIENTELEC.NS',
'ORIENTHOT.NS',
'ORIENTLTD.NS',
'ORIENTPPR.NS',
'ORIENTREF.NS',
'ORISSAMINE.NS',
'ORTEL.NS',
'OSWALAGRO.NS',
'PAEL.NS',
'PAGEIND.NS',
'PAISALO.NS',
'PALASHSECU.NS',
'PALREDTEC.NS',
'PANACEABIO.NS',
'PANACHE.NS',
'PANAMAPET.NS',
'PARABDRUGS.NS',
'PARACABLES.NS',
'PARAGMILK.NS',
'PARSVNATH.NS',
'PATELENG.NS',
'PATINTLOG.NS',
'PATSPINLTD.NS',
'PCJEWELLER.NS',
'PDMJEPAPER.NS',
'PDSMFL.NS',
'PEARLPOLY.NS',
'PEL.NS',
'PENIND.NS',
'PENINLAND.NS',
'PERSISTENT.NS',
'PETRONET.NS',
'PFC.NS',
'PFIZER.NS',
'PFOCUS.NS',
'PFS.NS',
'PGEL.NS',
'PGHH.NS',
'PGHL.NS',
'PGIL.NS',
'PHILIPCARB.NS',
'PHOENIXLTD.NS',
'PIDILITIND.NS',
'PIIND.NS',
'PILANIINVS.NS',
'PILITA.NS',
'PIONDIST.NS',
'PIONEEREMB.NS',
'PITTIENG.NS',
'PKTEA.NS',
'PLASTIBLEN.NS',
'PNB.NS',
'PNBGILTS.NS',
'PNBHOUSING.NS',
'PNC.NS',
'PNCINFRA.NS',
'PODDARHOUS.NS',
'PODDARMENT.NS',
'POKARNA.NS',
'POLYCAB.NS',
'POLYMED.NS',
'POLYPLEX.NS',
'PONNIERODE.NS',
'POWERGRID.NS',
'POWERINDIA.NS',
'POWERMECH.NS',
'PPAP.NS',
'PPL.NS',
'PRABHAT.NS',
'PRAENG.NS',
'PRAJIND.NS',
'PRAKASH.NS',
'PRAKASHSTL.NS',
'PRAXIS.NS',
'PRECAM.NS',
'PRECOT.NS',
'PRECWIRE.NS',
'PREMEXPLN.NS',
'PREMIER.NS',
'PREMIERPOL.NS',
'PRESSMN.NS',
'PRESTIGE.NS',
'PRICOLLTD.NS',
'PRIMESECU.NS',
'PRINCEPIPE.NS',
'PRIVISCL.NS',
'PROZONINTU.NS',
'PRSMJOHNSN.NS',
'PSB.NS',
'PSPPROJECT.NS',
'PTC.NS',
'PTL.NS',
'PUNJABCHEM.NS',
'PUNJLLOYD.NS',
'PURVA.NS',
'PVR.NS',
'QUESS.NS',
'QUICKHEAL.NS',
'RADAAN.NS',
'RADICO.NS',
'RADIOCITY.NS',
'RAIN.NS',
'RAJESHEXPO.NS',
'RAJRATAN.NS',
'RAJRAYON.NS',
'RAJSREESUG.NS',
'RAJTV.NS',
'RALLIS.NS',
'RAMANEWS.NS',
'RAMASTEEL.NS',
'RAMCOCEM.NS',
'RAMCOIND.NS',
'RAMCOSYS.NS',
'RAMKY.NS',
'RAMSARUP.NS',
'RANASUG.NS',
'RANEENGINE.NS',
'RANEHOLDIN.NS',
'RATNAMANI.NS',
'RAYMOND.NS',
'RBL.NS',
'RBLBANK.NS',
'RCF.NS',
'RCOM.NS',
'RECLTD.NS',
'REDINGTON.NS',
'REFEX.NS',
'RELAXO.NS',
'RELCAPITAL.NS',
'RELIANCE.NS',
'RELIGARE.NS',
'RELINFRA.NS',
'REMSONSIND.NS',
'RENUKA.NS',
'REPCOHOME.NS',
'REPL.NS',
'REPRO.NS',
'RESPONIND.NS',
'REVATHI.NS',
'RGL.NS',
'RHFL.NS',
'RICOAUTO.NS',
'RIIL.NS',
'RITES.NS',
'RKDL.NS',
'RKEC.NS',
'RKFORGE.NS',
'RMCL.NS',
'RML.NS',
'RNAVAL.NS',
'ROHITFERRO.NS',
'ROHLTD.NS',
'ROLLT.NS',
'ROLTA.NS',
'ROML.NS',
'ROSSARI.NS',
'ROSSELLIND.NS',
'ROUTE.NS',
'RPGLIFE.NS',
'RPOWER.NS',
'RPPINFRA.NS',
'RSSOFTWARE.NS',
'RSWM.NS',
'RSYSTEMS.NS',
'RTNINFRA.NS',
'RTNPOWER.NS',
'RUBYMILLS.NS',
'RUCHI.NS',
'RUCHINFRA.NS',
'RUCHIRA.NS',
'RUPA.NS',
'RUSHIL.NS',
'RVHL.NS',
'RVNL.NS',
'S&SPOWER.NS',
'SABEVENTS.NS',
'SADBHAV.NS',
'SADBHIN.NS',
'SAFARI.NS',
'SAGARDEEP.NS',
'SAGCEM.NS',
'SAIL.NS',
'SAKAR.NS',
'SAKHTISUG.NS',
'SAKSOFT.NS',
'SAKUMA.NS',
'SALASAR.NS',
'SALONA.NS',
'SALSTEEL.NS',
'SALZERELEC.NS',
'SAMBHAAV.NS',
'SANCO.NS',
'SANDESH.NS',
'SANDHAR.NS',
'SANGAMIND.NS',
'SANGHIIND.NS',
'SANGHVIFOR.NS',
'SANGHVIMOV.NS',
'SANGINITA.NS',
'SANOFI.NS',
'SANWARIA.NS',
'SARDAEN.NS',
'SAREGAMA.NS',
'SARLAPOLY.NS',
'SASKEN.NS',
'SASTASUNDR.NS',
'SATIA.NS',
'SATIN.NS',
'SBICARD.NS',
'SBILIFE.NS',
'SBIN.NS',
'SCAPDVR.NS',
'SCHAEFFLER.NS',
'SCHAND.NS',
'SCHNEIDER.NS',
'SCI.NS',
'SDBL.NS',
'SEAMECLTD.NS',
'SELAN.NS',
'SELMCL.NS',
'SEPOWER.NS',
'SEQUENT.NS',
'SESHAPAPER.NS',
'SETCO.NS',
'SETUINFRA.NS',
'SEYAIND.NS',
'SEZAL.NS',
'SFL.NS',
'SGL.NS',
'SHAHALLOYS.NS',
'SHAKTIPUMP.NS',
'SHALBY.NS',
'SHALPAINTS.NS',
'SHANKARA.NS',
'SHANTIGEAR.NS',
'SHARDACROP.NS',
'SHARDAMOTR.NS',
'SHAREINDIA.NS',
'SHEMAROO.NS',
'SHIL.NS',
'SHILPAMED.NS',
'SHIRPUR-G.NS',
'SHIVAMAUTO.NS',
'SHIVAMILLS.NS',
'SHIVATEX.NS',
'SHK.NS',
'SHOPERSTOP.NS',
'SHRADHA.NS',
'SHREDIGCEM.NS',
'SHREECEM.NS',
'SHREEPUSHK.NS',
'SHREERAMA.NS',
'SHRENIK.NS',
'SHREYANIND.NS',
'SHREYAS.NS',
'SHRIPISTON.NS',
'SHRIRAMCIT.NS',
'SHRIRAMEPC.NS',
'SHYAMCENT.NS',
'SHYAMTEL.NS',
'SICAGEN.NS',
'SICAL.NS',
'SIEMENS.NS',
'SIGIND.NS',
'SIL.NS',
'SILINV.NS',
'SILLYMONKS.NS',
'SIMBHALS.NS',
'SIMPLEXINF.NS',
'SINTERCOM.NS',
'SINTEX.NS',
'SIRCA.NS',
'SIS.NS',
'SITINET.NS',
'SIYSIL.NS',
'SJVN.NS',
'SKFINDIA.NS',
'SKIL.NS',
'SKIPPER.NS',
'SKMEGGPROD.NS',
'SMARTLINK.NS',
'SMLISUZU.NS',
'SMPL.NS',
'SMSLIFE.NS',
'SMSPHARMA.NS',
'SNOWMAN.NS',
'SOBHA.NS',
'SOLARA.NS',
'SOLARINDS.NS',
'SOMANYCERA.NS',
'SOMATEX.NS',
'SOMICONVEY.NS',
'SONATSOFTW.NS',
'SORILINFRA.NS',
'SOTL.NS',
'SOUTHBANK.NS',
'SOUTHWEST.NS',
'SPAL.NS',
'SPANDANA.NS',
'SPARC.NS',
'SPECIALITY.NS',
'SPENCERS.NS',
'SPENTEX.NS',
'SPIC.NS',
'SPICEJET.NS',
'SPLIL.NS',
'SPMLINFRA.NS',
'SPTL.NS',
'SREEL.NS',
'SREINFRA.NS',
'SRF.NS',
'SRHHYPOLTD.NS',
'SRIPIPES.NS',
'SRPL.NS',
'SRTRANSFIN.NS',
'SSWL.NS',
'STAR.NS',
'STARCEMENT.NS',
'STARPAPER.NS',
'STCINDIA.NS',
'STEELCITY.NS',
'STEELXIND.NS',
'STEL.NS',
'STERTOOLS.NS',
'STLTECH.NS',
'SUBCAPCITY.NS',
'SUBEXLTD.NS',
'SUBROS.NS',
'SUDARSCHEM.NS',
'SUJANAUNI.NS',
'SUMICHEM.NS',
'SUMIT.NS',
'SUMMITSEC.NS',
'SUNCLAYLTD.NS',
'SUNDARAM.NS',
'SUNDARMFIN.NS',
'SUNDARMHLD.NS',
'SUNDRMBRAK.NS',
'SUNDRMFAST.NS',
'SUNFLAG.NS',
'SUNPHARMA.NS',
'SUNTECK.NS',
'SUNTV.NS',
'SUPERHOUSE.NS',
'SUPERSPIN.NS',
'SUPPETRO.NS',
'SUPRAJIT.NS',
'SUPREMEENG.NS',
'SUPREMEIND.NS',
'SUPREMEINF.NS',
'SURANASOL.NS',
'SURANAT&P.NS',
'SURYALAXMI.NS',
'SURYAROSNI.NS',
'SUTLEJTEX.NS',
'SUULD.NS',
'SUVEN.NS',
'SUVENPHAR.NS',
'SUZLON.NS',
'SWANENERGY.NS',
'SWARAJENG.NS',
'SWELECTES.NS',
'SWSOLAR.NS',
'SYMPHONY.NS',
'SYNCOM.NS',
'SYNGENE.NS',
'TAINWALCHM.NS',
'TAJGVK.NS',
'TAKE.NS',
'TALBROAUTO.NS',
'TANLA.NS',
'TANTIACONS.NS',
'TARC.NS',
'TARMAT.NS',
'TASTYBITE.NS',
'TATACHEM.NS',
'TATACOFFEE.NS',
'TATACOMM.NS',
'TATACONSUM.NS',
'TATAELXSI.NS',
'TATAINVEST.NS',
'TATAMETALI.NS',
'TATAMOTORS.NS',
'TATAMTRDVR.NS',
'TATAPOWER.NS',
'TATASTEEL.NS',
'TATASTLBSL.NS',
'TATASTLLP.NS',
'TBZ.NS',
'TCI.NS',
'TCIDEVELOP.NS',
'TCIEXP.NS',
'TCIFINANCE.NS',
'TCNSBRANDS.NS',
'TCPLPACK.NS',
'TCS.NS',
'TDPOWERSYS.NS',
'TEAMLEASE.NS',
'TECHIN.NS',
'TECHM.NS',
'TECHNOE.NS',
'TECHNOFAB.NS',
'TEJASNET.NS',
'TERASOFT.NS',
'TEXINFRA.NS',
'TEXMOPIPES.NS',
'TEXRAIL.NS',
'TFCILTD.NS',
'TFL.NS',
'TGBHOTELS.NS',
'THANGAMAYL.NS',
'THEINVEST.NS',
'THEMISMED.NS',
'THERMAX.NS',
'THIRUSUGAR.NS',
'THOMASCOOK.NS',
'THOMASCOTT.NS',
'THYROCARE.NS',
'TI.NS',
'TIDEWATER.NS',
'TIIL.NS',
'TIINDIA.NS',
'TIJARIA.NS',
'TIL.NS',
'TIMESGTY.NS',
'TIMETECHNO.NS',
'TIMKEN.NS',
'TINPLATE.NS',
'TIPSINDLTD.NS',
'TIRUMALCHM.NS',
'TIRUPATIFL.NS',
'TITAN.NS',
'TMRVL.NS',
'TNPETRO.NS',
'TNPL.NS',
'TNTELE.NS',
'TOKYOPLAST.NS',
'TORNTPHARM.NS',
'TORNTPOWER.NS',
'TOTAL.NS',
'TOUCHWOOD.NS',
'TPLPLASTEH.NS',
'TREEHOUSE.NS',
'TREJHARA.NS',
'TRENT.NS',
'TRF.NS',
'TRIDENT.NS',
'TRIGYN.NS',
'TRIL.NS',
'TRITURBINE.NS',
'TRIVENI.NS',
'TTKHLTCARE.NS',
'TTKPRESTIG.NS',
'TTL.NS',
'TTML.NS',
'TV18BRDCST.NS',
'TVSELECT.NS',
'TVSMOTOR.NS',
'TVSSRICHAK.NS',
'TVTODAY.NS',
'TVVISION.NS',
'TWL.NS',
'UBL.NS',
'UCALFUEL.NS',
'UCOBANK.NS',
'UFLEX.NS',
'UFO.NS',
'UGARSUGAR.NS',
'UJAAS.NS',
'UJJIVAN.NS',
'UJJIVANSFB.NS',
'ULTRACEMCO.NS',
'UMANGDAIRY.NS',
'UMESLTD.NS',
'UNICHEMLAB.NS',
'UNIDT.NS',
'UNIENTER.NS',
'UNIONBANK.NS',
'UNITECH.NS',
'UNITEDTEA.NS',
'UNITY.NS',
'UNIVASTU.NS',
'UNIVCABLES.NS',
'UNIVPHOTO.NS',
'UPL.NS',
'URJA.NS',
'USHAMART.NS',
'UTIAMC.NS',
'UTTAMSTL.NS',
'UTTAMSUGAR.NS',
'V2RETAIL.NS',
'VADILALIND.NS',
'VAIBHAVGBL.NS',
'VAISHALI.NS',
'VAKRANGEE.NS',
'VALIANTORG.NS',
'VARDHACRLC.NS',
'VARDMNPOLY.NS',
'VARROC.NS',
'VASCONEQ.NS',
'VASWANI.NS',
'VBL.NS',
'VEDL.NS',
'VENKEYS.NS',
'VENUSREM.NS',
'VERTOZ.NS',
'VESUVIUS.NS',
'VETO.NS',
'VGUARD.NS',
'VHL.NS',
'VICEROY.NS',
'VIDEOIND.NS',
'VIDHIING.NS',
'VIJIFIN.NS',
'VIKASECO.NS',
'VIKASMCORP.NS',
'VIKASPROP.NS',
'VIKASWSP.NS',
'VIMTALABS.NS',
'VINATIORGA.NS',
'VINDHYATEL.NS',
'VINYLINDIA.NS',
'VIPCLOTHNG.NS',
'VIPIND.NS',
'VIPULLTD.NS',
'VISAKAIND.NS',
'VISASTEEL.NS',
'VISHAL.NS',
'VISHNU.NS',
'VISHWARAJ.NS',
'VIVIDHA.NS',
'VIVIMEDLAB.NS',
'VLSFINANCE.NS',
'VMART.NS',
'VOLTAMP.NS',
'VOLTAS.NS',
'VRLLOG.NS',
'VSSL.NS',
'VSTIND.NS',
'VSTTILLERS.NS',
'VTL.NS',
'WABAG.NS',
'WABCOINDIA.NS',
'WALCHANNAG.NS',
'WANBURY.NS',
'WATERBASE.NS',
'WEBELSOLAR.NS',
'WEIZMANIND.NS',
'WELCORP.NS',
'WELENT.NS',
'WELINV.NS',
'WELSPUNIND.NS',
'WENDT.NS',
'WESTLIFE.NS',
'WHEELS.NS',
'WHIRLPOOL.NS',
'WILLAMAGOR.NS',
'WINDMACHIN.NS',
'WIPL.NS',
'WIPRO.NS',
'WOCKPHARMA.NS',
'WONDERLA.NS',
'WORTH.NS',
'WSI.NS',
'WSTCSTPAPR.NS',
'XCHANGING.NS',
'XELPMOC.NS',
'XPROINDIA.NS',
'YAARII.NS',
'YESBANK.NS',
'ZEEL.NS',
'ZEELEARN.NS',
'ZEEMEDIA.NS',
'ZENITHEXPO.NS',
'ZENITHSTL.NS',
'ZENSARTECH.NS',
'ZENTEC.NS',
'ZICOM.NS',
'ZODIACLOTH.NS',
'ZODJRDMKJ.NS',
'ZOTA.NS',
'ZUARI.NS',
'ZUARIGLOB.NS',
'ZYDUSWELL.NS' ]

selected_tickers = st.multiselect('Select Tickers', default_tickers)

# Validate if tickers are selected
if len(selected_tickers) < 2:
    st.error('Please select at least 2 tickers.')
else:
    # Download data based on user input
    df = yf.download(selected_tickers, start=start_date, end=end_date)['Adj Close']

    # Calculate daily percentage change in adjusted close prices
    returns = df.pct_change(fill_method=None)

    # Calculate the correlation matrix
    correlation_matrix = returns.corr()

    # Display the correlation matrix
    st.write("Correlation Matrix:")
    st.write(correlation_matrix)

    # Plot the correlation heatmap using Seaborn
    colors = [(0, '#800000'),
              (0.25, '#FFFFcc'),  # Red
          (0.5, '#004d00'),
            (0.75, '#FFFFcc'),  # Green
          (1, '#800000')]  # Red
    cmap = LinearSegmentedColormap.from_list('custom', colors)
    
    plt.figure(figsize=(10, 8))
    #sns.diverging_palette(250, 30, l=65, center="dark", as_cmap=True)
    sns.heatmap(correlation_matrix, annot=True,cmap=cmap, cbar=True, vmax=1, vmin=-1)
    plt.title('\nCorrelation Heatmap\n')

    # Show the plot in Streamlit
    st.pyplot(plt)

    for ticker in selected_tickers:
        st.write(f"Closing Prices for {ticker}")
        plt.figure(figsize=(10, 5))
        plt.plot(df.index, df[ticker], label=ticker)
        plt.title(f'Closing Price of {ticker} from {from_date} to {to_date}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)
