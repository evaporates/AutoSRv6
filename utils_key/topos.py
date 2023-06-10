#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：AutoSRv6 
@File ：topos.py
@Author ：Lucky
@Date ：2023/3/9 17:10
'''
import random
import time

files = [
        'Aarnet.graphml',
        'Abilene.graphml',
        'Abvt.graphml',
        'Aconet.graphml',
        'Agis.graphml',
        'Ai3.graphml',
        'Airtel.graphml',
        'Amres.graphml',
        'Ans.graphml',
        'Arn.graphml',
        'Arnes.graphml',
        'Arpanet19706.graphml',
        'Arpanet19719.graphml',
        'Arpanet19723.graphml',
        'Arpanet19728.graphml',
        'Arpanet196912.graphml',
        'AsnetAm.graphml',
        'Atmnet.graphml',
        'AttMpls.graphml',
        'Azrena.graphml',
        'Bandcon.graphml',
        'Basnet.graphml',
        'Bbnplanet.graphml',
        'Bellcanada.graphml',
        'Bellsouth.graphml',
        'Belnet2003.graphml',
        'Belnet2004.graphml',
        'Belnet2005.graphml',
        'Belnet2006.graphml',
        'Belnet2007.graphml',
        'Belnet2008.graphml',
        'Belnet2009.graphml',
        'Belnet2010.graphml',
        'BeyondTheNetwork.graphml',
        'Bics.graphml',
        'Biznet.graphml',
        'Bren.graphml',
        'BsonetEurope.graphml',
        'BtAsiaPac.graphml',
        'BtEurope.graphml',
        'BtLatinAmerica.graphml',
        'BtNorthAmerica.graphml',
        'Canerie.graphml',
        'Carnet.graphml',
        'Cernet.graphml',
        'Cesnet1993.graphml',
        'Cesnet1997.graphml',
        'Cesnet1999.graphml',
        'Cesnet2001.graphml',
        'Cesnet200304.graphml',
        'Cesnet200511.graphml',
        'Cesnet200603.graphml',
        'Cesnet200706.graphml',
        'Cesnet201006.graphml',
        'Chinanet.graphml',
        'Claranet.graphml',
        'Cogentco.graphml',
        'Colt.graphml',
        'Columbus.graphml',
        'Compuserve.graphml',
        'CrlNetworkServices.graphml',
        'Cudi.graphml',
        'Cwix.graphml',
        'Cynet.graphml',
        'Darkstrand.graphml',
        'Dataxchange.graphml',
        'Deltacom.graphml',
        'DeutscheTelekom.graphml',
        'Dfn.graphml',
        'DialtelecomCz.graphml',
        'Digex.graphml',
        'Easynet.graphml',
        'Eenet.graphml',
        'EliBackbone.graphml',
        'Epoch.graphml',
        'Ernet.graphml',
        'Esnet.graphml',
        'Eunetworks.graphml',
        'Evolink.graphml',
        'Fatman.graphml',
        'Fccn.graphml',
        'Fccn.graphml',
        'Funet.graphml',
        'Gambia.graphml',
        'Garr199901.graphml',
        'Garr199904.graphml',
        'Garr199905.graphml',
        'Garr200109.graphml',
        'Garr200112.graphml',
        'Garr200212.graphml',
        'Garr200404.graphml',
        'Garr200902.graphml',
        'Garr200908.graphml',
        'Garr200909.graphml',
        'Garr200912.graphml',
        'Garr201001.graphml',
        'Garr201003.graphml',
        'Garr201004.graphml',
        'Garr201005.graphml',
        'Garr201007.graphml',
        'Garr201008.graphml',
        'Garr201010.graphml',
        'Garr201012.graphml',
        'Garr201101.graphml',
        'Garr201102.graphml',
        'Garr201103.graphml',
        'Garr201104.graphml',
        'Garr201105.graphml',
        'Garr201107.graphml',
        'Garr201108.graphml',
        'Garr201109.graphml',
        'Garr201110.graphml',
        'Garr201111.graphml',
        'Garr201112.graphml',
        'Garr201201.graphml',
        'Gblnet.graphml',
        'Geant2001.graphml',
        'Geant2009.graphml',
        'Geant2010.graphml',
        'Geant2012.graphml',
        'Getnet.graphml',
        'Globalcenter.graphml',
        'Globenet.graphml',
        'Goodnet.graphml',
        'Grena.graphml',
        'Grnet.graphml',
        'GtsCe.graphml',
        'GtsCzechRepublic.graphml',
        'GtsHungary.graphml',
        'GtsPoland.graphml',
        'GtsRomania.graphml',
        'GtsSlovakia.graphml',
        'Harnet.graphml',
        'Heanet.graphml',
        'HiberniaCanada.graphml',
        'HiberniaGlobal.graphml',
        'HiberniaIreland.graphml',
        'HiberniaNireland.graphml',
        'HiberniaUk.graphml',
        'HiberniaUs.graphml',
        'Highwinds.graphml',
        'HostwayInternational.graphml',
        'HurricaneElectric.graphml',
        'Ibm.graphml',
        'Iij.graphml',
        'Iinet.graphml',
        'Ilan.graphml',
        'Integra.graphml',
        'Intellifiber.graphml',
        'Internetmci.graphml',
        'Internode.graphml',
        'Interoute.graphml',
        'Intranetwork.graphml',
        'Ion.graphml',
        'IowaStatewideFiberMap.graphml',
        'Iris.graphml',
        'Istar.graphml',
        'Itnet.graphml',
        'Janetbackbone.graphml',
        'JanetExternal.graphml',
        'Janetlense.graphml',
        'Jgn2Plus.graphml',
        'Karen.graphml',
        'Kdl.graphml',
        'KentmanApr2007.graphml',
        'KentmanAug2005.graphml',
        'KentmanFeb2008.graphml',
        'KentmanJan2011.graphml',
        'KentmanJul2005.graphml',
        'Kreonet.graphml',
        'LambdaNet.graphml',
        'Latnet.graphml',
        'Layer42.graphml',
        'Litnet.graphml',
        'Marnet.graphml',
        'Marwan.graphml',
        'Missouri.graphml',
        'Mren.graphml',
        'Myren.graphml',
        'Napnet.graphml',
        'Navigata.graphml',
        'Netrail.graphml',
        'NetworkUsa.graphml',
        'Nextgen.graphml',
        'Niif.graphml',
        'Noel.graphml',
        'Nordu1989.graphml',
        'Nordu1997.graphml',
        'Nordu2005.graphml',
        'Nordu2010.graphml',
        'Nsfcnet.graphml',
        'Ntelos.graphml',
        'Ntt.graphml',
        'Oteglobe.graphml',
        'Oxford.graphml',
        'Pacificwave.graphml',
        'Packetexchange.graphml',
        'Padi.graphml',
        'Palmetto.graphml',
        'Peer1.graphml',
        'Pern.graphml',
        'PionierL1.graphml',
        'PionierL3.graphml',
        'Psinet.graphml',
        'Quest.graphml',
        'RedBestel.graphml',
        'Rediris.graphml',
        'Renam.graphml',
        'Renater1999.graphml',
        'Renater2001.graphml',
        'Renater2004.graphml',
        'Renater2006.graphml',
        'Renater2008.graphml',
        'Renater2010.graphml',
        'Restena.graphml',
        'Reuna.graphml',
        'Rhnet.graphml',
        'Rnp.graphml',
        'Roedunet.graphml',
        'RoedunetFibre.graphml',
        'Sago.graphml',
        'Sanet.graphml',
        'Sanren.graphml',
        'Savvis.graphml',
        'Shentel.graphml',
        'Sinet.graphml',
        'Singaren.graphml',
        'Spiralight.graphml',
        'Sprint.graphml',
        'Sunet.graphml',
        'Surfnet.graphml',
        'Switch.graphml',
        'SwitchL3.graphml',
        'Syringa.graphml',
        'TataNld.graphml',
        'Telcove.graphml',
        'Telecomserbia.graphml',
        'Tinet.graphml',
        'TLex.graphml',
        'Tw.graphml',
        'Twaren.graphml',
        'Ulaknet.graphml',
        'UniC.graphml',
        'Uninet.graphml',
        'Uninett2010.graphml',
        'Uninett2011.graphml',
        'Uran.graphml',
        'UsCarrier.graphml',
        'UsSignal.graphml',
        'Uunet.graphml',
        'Vinaren.graphml',
        'VisionNet.graphml',
        'VtlWavenet2008.graphml',
        'VtlWavenet2011.graphml',
        'VtlWavenet2011.graphml',
        'WideJpn.graphml',
        'Xeex.graphml',
        'York.graphml',
        'Zamren.graphml',

    ]
def output():
        sleep_time = random.uniform(0.2, 1.51)  # 生成随机的休眠时间
        time.sleep(sleep_time)