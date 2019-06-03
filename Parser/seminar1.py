from pyparsing import *
import json
# define grammar
'''
gloss ::= 'gloss' character 
lemma ::= 'lemma=\' character 
msd ::= 'msd=\' character 
tag ::= 'tag=\' character 
n ::='in=\' character 
out ::= 'out=\' character 
trazeno = '<W' gloss lemma msd tag in out '>' character '</W>'
'''
gloss = Combine(Suppress('<W gloss="')+Word(alphas)+Optional('-') + Optional('_')+ZeroOrMore(Word(alphas)))
lemma = Combine(Suppress('lemma="')+ Word(printables))
msd = Combine(Suppress('msd="')+Word(printables))
tag = Combine(Suppress('tag="')+Word(alphanums))
in_ = Combine(Suppress('in="')+Optional('-') + Word(nums,exact=1) + ':' + Word(alphas))
out = Combine(Suppress('out="')+Optional('-')+OneOrMore(OneOrMore(Word(nums))+':'+Word(alphas)+Optional('|')))
tekst1="""<W gloss="Two" lemma="to" msd="AC---U=--" tag="CD" in="9:subj" out="1:attr|2:attr|3:nobj|5:appr">To</W>
<W gloss="well-known" lemma="kendt" msd="ANP[CN]PU=[DI]U" tag="JJ" in="-1:attr" out="">kendte</W>
<W gloss="Russian" lemma="russisk" msd="ANP[CN]PU=[DI]U" tag="JJ" in="-2:attr" out="">russiske</W>
<W gloss="historians" lemma="historiker" msd="NCCPU==I" tag="NNP" in="-3:nobj" out="">historikere</W>
<W gloss="Andronik" lemma="Andronik" msd="NP--U==-" tag="NNP" in="1:namef" out="">Andronik</W>
<W gloss="Mirganjan" lemma="Mirganjan" msd="NP--U==-" tag="NNP" in="-5:appr" out="-1:namef|3:conj">Mirganjan</W>
<W gloss="and" lemma="og" msd="CC" tag="CC" in="2:coord" out="">og</W>
<W gloss="Igor" lemma="Igor" msd="NP--U==-" tag="NNP" in="1:namef" out="">Igor</W>
<W gloss="Klamkin" lemma="Klamkin" msd="NP--U==-" tag="NNP" in="-3:conj" out="-1:namef|-2:coord">Klamkin</W>
<W gloss="do_believe" lemma="tro" msd="VADR=----A-" tag="VBD" in="" out="-9:subj|1:neg|2:pnct|3:dobj|12:pnct">tror</W>
<W gloss="not" lemma="ikke" msd="RGU" tag="RP" in="-1:neg" out="">ikke</W>
<W gloss="," lemma="," msd="XP" tag="," in="-2:pnct" out="">,</W>
<W gloss="that" lemma="at" msd="CS" tag="IN" in="-3:dobj" out="2:vobj">at</W>
<W gloss="Russia" lemma="Rusland" msd="NP--U==-" tag="NNP" in="1:subj|2:[subj]" out="">Rusland</W>
<W gloss="can" lemma="kunne" msd="VADR=----A-" tag="VBD" in="-2:vobj" out="-1:subj|1:vobj|2:other">kan</W>
<W gloss="be_developed" lemma="udvikle" msd="VAF-=----P-" tag="VB" in="-1:vobj" out="-2:[subj]">udvikles</W>
<W gloss="without" lemma="uden" msd="SP" tag="IN" in="-2:other" out="1:nobj">uden</W>
<W gloss="an" lemma="en" msd="PI-CSU--U" tag="DT" in="-1:nobj" out="2:nobj">en</W>
<W gloss="&amp;quot;" lemma="&amp;quot;" msd="XP" tag="&amp;quot;" in="1:pnct" out="">"</W>
<W gloss="iron_fist" lemma="jernnæve" msd="NCCSU==I" tag="NN" in="-2:nobj" out="-1:pnct|1:pnct">jernnæve</W>
<W gloss="&amp;quot;" lemma="&amp;quot;" msd="XP" tag="&amp;quot;" in="-1:pnct" out="">"</W>
<W gloss="." lemma="." msd="XP" tag="." in="-12:pnct" out="">.</W>

<W gloss="They" lemma="de" msd="PP3[CN]PN-NU" tag="PRP" in="1:subj" out="">De</W>
<W gloss="claim" lemma="hævde" msd="VADR=----A-" tag="VBD" in="" out="-1:subj|1:pnct|2:dobj|10:pnct">hævder</W>
<W gloss="," lemma="," msd="XP" tag="," in="-1:pnct" out="">,</W>
<W gloss="that" lemma="at" msd="CS" tag="IN" in="-2:dobj" out="5:vobj">at</W>
<W gloss="Russia's" lemma="Rusland" msd="NP--G==-" tag="NNP" in="4:subj" out="1:possd">Ruslands</W>
<W gloss="path" lemma="vej" msd="NCCSU==I" tag="NN" in="-1:possd" out="1:@dir">vej</W>
<W gloss="to" lemma="til" msd="SP" tag="IN" in="-1:@dir" out="1:nobj">til</W>
<W gloss="democracy" lemma="demokrati" msd="NCNSU==I" tag="NN" in="-1:nobj" out="">demokrati</W>
<W gloss="goes" lemma="gå" msd="VADR=----A-" tag="VBD" in="-5:vobj" out="-4:subj|1:@dir">går</W>
<W gloss="through" lemma="gennem" msd="SP" tag="IN" in="-1:@dir" out="1:nobj">gennem</W>
<W gloss="dictatorship" lemma="diktatur" msd="NCNSU==I" tag="NN" in="-1:nobj" out="">diktatur</W>
<W gloss="." lemma="." msd="XP" tag="." in="-10:pnct" out="">.</W>

<W gloss="In" lemma="i" msd="SP" tag="IN" in="5:loc" out="1:nobj">I</W>
<W gloss="one" lemma="en" msd="PI-CSU--U" tag="DT" in="-1:nobj" out="1:pobj">en</W>
<W gloss="of" lemma="af" msd="SP" tag="IN" in="-1:pobj" out="1:nobj">af</W>
<W gloss="their" lemma="deres" msd="PO3[CN][SP]UPNU" tag="PRP$" in="-1:nobj" out="1:possd">deres</W>
<W gloss="articles" lemma="artikel" msd="NCCPU==I" tag="NNP" in="-1:possd" out="">artikler</W>
<W gloss="says" lemma="hedde" msd="VADR=----A-" tag="VBD" in="" out="-5:loc|1:subj|2:pnct|8:qobj|14:pnct">hedder</W>
<W gloss="it" lemma="det" msd="PP3NSU-NU" tag="PRP" in="-1:subj" out="">det</W>
<W gloss="&3a;" lemma="&3a;" msd="XP" tag="&3a;" in="-2:pnct" out="">:</W>
<W gloss="&amp;quot;" lemma="&amp;quot;" msd="XP" tag="&amp;quot;" in="5:pnct" out="">"</W>
<W gloss="In" lemma="i" msd="SP" tag="IN" in="4:loc" out="1:nobj">I</W>
<W gloss="an" lemma="en" msd="PI-NSU--U" tag="DT" in="-1:nobj" out="1:attr|2:nobj">et</W>
<W gloss="authoritarian" lemma="autoritær" msd="ANPNSU=IU" tag="JJ" in="-1:attr" out="">autoritært</W>
<W gloss="regime" lemma="regime" msd="NCNSU==I" tag="NN" in="-2:nobj" out="">regime</W>
<W gloss="lagdel" lemma="lagdel" msd="XX" tag="FW" in="-8:qobj" out="-5:pnct|-4:loc|1:subj|5:conj">lagdel</W>
<W gloss="society" lemma="samfund" msd="NCNSU==D" tag="NN" in="-1:subj" out="">samfundet</W>
<W gloss="and" lemma="og" msd="CC" tag="CC" in="3:coord" out="">og</W>
<W gloss="different" lemma="forskellig" msd="ANP[CN]PU=[DI]U" tag="JJ" in="1:attr" out="">forskellige</W>
<W gloss="interests" lemma="interesse" msd="NCCPU==I" tag="NNP" in="1:subj" out="-1:attr">interesser</W>
<W gloss="matured" lemma="modne" msd="VADR=----P-" tag="VBD" in="-5:conj" out="-1:subj|-3:coord">modnes</W>
<W gloss="." lemma="." msd="XP" tag="." in="-14:pnct" out="">.</W>

<W gloss="And" lemma="og" msd="CC" tag="CC" in="" out="15:conj|20:pnct">Og</W>
<W gloss="when" lemma="når" msd="CS" tag="IN" in="14:xtop" out="3:vobj|13:ref">når</W>
<W gloss="their" lemma="deres" msd="PO3[CN][SP]UPNU" tag="PRP$" in="2:subj" out="1:possd">deres</W>
<W gloss="representatives" lemma="repræsentant" msd="NCCPU==I" tag="NNP" in="-1:possd" out="">repræsentanter</W>
<W gloss="are" lemma="være" msd="VADR=----A-" tag="VBD" in="-3:vobj" out="-2:subj|1:preds|9:pnct">er</W>
<W gloss="ready" lemma="parat" msd="ANP[CN]PU=[DI]U" tag="JJ" in="-1:preds" out="1:pobj">parate</W>
<W gloss="in" lemma="til" msd="SP" tag="IN" in="-1:pobj" out="1:nobj">til</W>
<W gloss="that" lemma="at" msd="U=" tag="TO" in="-1:nobj" out="1:vobj">at</W>
<W gloss="go" lemma="gå" msd="VAF-=----A-" tag="VB" in="-1:vobj" out="1:@loc">gå</W>
<W gloss="in" lemma="i" msd="SP" tag="IN" in="-1:@loc" out="1:nobj">i</W>
<W gloss="struben" lemma="strube" msd="NCCSU==D" tag="NN" in="-1:nobj" out="1:pobj">struben</W>
<W gloss="in" lemma="på" msd="SP" tag="IN" in="-1:pobj" out="1:nobj">på</W>
<W gloss="each_other" lemma="hinanden" msd="PC--PU---" tag="PP" in="-1:nobj" out="">hinanden</W>
<W gloss="," lemma="," msd="XP" tag="," in="-9:pnct" out="">,</W>
<W gloss="so" lemma="så" msd="RGU" tag="RP" in="-13:ref|1:other" out="">så</W>
<W gloss="puts_a_stop_to" lemma="stoppe" msd="VADR=----A-" tag="VBD" in="-15:conj" out="-14:xtop|-1:other|1:subj|3:pnct|4:dobj">stopper</W>
<W gloss="an" lemma="en" msd="PI-CSU--U" tag="DT" in="-1:subj" out="1:nobj">en</W>
<W gloss="iron_fist" lemma="jernnæve" msd="NCCSU==I" tag="NN" in="-1:nobj" out="">jernnæve</W>
<W gloss="'" lemma="&amp;quot;" msd="XP" tag="&amp;quot;" in="-3:pnct" out="">"</W>
<W gloss="it" lemma="det" msd="PP3NSU-NU" tag="PRP" in="-4:dobj" out="">det</W>
<W gloss="." lemma="." msd="XP" tag="." in="-20:pnct" out="">.</W>

<W gloss="In" lemma="på" msd="SP" tag="IN" in="3:man" out="1:nobj">På</W>
<W gloss="this" lemma="den" msd="PD-CSU--U" tag="DT" in="-1:nobj" out="1:nobj">den</W>
<W gloss="way" lemma="måde" msd="NCCSU==I" tag="NN" in="-1:nobj" out="">måde</W>
<W gloss="are_created" lemma="skabe" msd="VADR=----P-" tag="VBD" in="" out="-3:man|1:other|3:subj|9:coord|14:pnct|15:pnct">skabes</W>
<W gloss="the_whole" lemma="hel" msd="ANP[CN]SU=DU" tag="JJ" in="-1:other" out="1:nobj">hele</W>
<W gloss="the_time" lemma="tid" msd="NCCSU==D" tag="NN" in="-1:nobj" out="">tiden</W>
<W gloss="the_conditions" lemma="betingelse" msd="NCCPU==D" tag="NNP" in="-3:subj" out="1:pobj">betingelserne</W>
<W gloss="for" lemma="for" msd="SP" tag="IN" in="-1:pobj" out="1:nobj">for</W>
<W gloss="a" lemma="en" msd="PI-CSU--U" tag="DT" in="-1:nobj" out="1:nobj">en</W>
<W gloss="harmonization" lemma="harmonisering" msd="NCCSU==I" tag="NN" in="-1:nobj" out="1:pobj">harmonisering</W>
<W gloss="of" lemma="af" msd="SP" tag="IN" in="-1:pobj" out="1:nobj">af</W>
<W gloss="interests" lemma="interesse" msd="NCCPU==I" tag="NNP" in="-1:nobj" out="">interesser</W>
<W gloss="and" lemma="og" msd="CC" tag="CC" in="-9:coord" out="1:&lt;mod&gt;|2:&lt;subj&3a;pobj&gt;">og</W>
<W gloss="consequently" lemma="følgelig" msd="RGU" tag="RP" in="-1:&lt;mod&gt;" out="">følgelig</W>
<W gloss="for" lemma="for" msd="SP" tag="IN" in="-2:&lt;subj&3a;pobj&gt;" out="2:nobj">for</W>
<W gloss="democratic" lemma="demokratisk" msd="ANP[CN]PU=[DI]U" tag="JJ" in="1:attr" out="">demokratiske</W>
<W gloss="reforms" lemma="reform" msd="NCCPU==I" tag="NNP" in="-2:nobj" out="-1:attr">reformer</W>
<W gloss="&amp;quot;" lemma="&amp;quot;" msd="XP" tag="&amp;quot;" in="-14:pnct" out="">"</W>
<W gloss="." lemma="." msd="XP" tag="." in="-15:pnct" out="">.</W>

<W gloss="And" lemma="og" msd="CC" tag="CC" in="" out="2:conj">Og</W>
<W gloss="they" lemma="de" msd="PP3[CN]PN-NU" tag="PRP" in="1:subj" out="">de</W>
<W gloss="added" lemma="tilføje" msd="VADA=----A-" tag="VBD" in="-2:conj" out="-1:subj|1:pnct|15:qobj">tilføjede</W>
<W gloss="&3a;" lemma="&3a;" msd="XP" tag="&3a;" in="-1:pnct" out="">:</W>
<W gloss="&amp;quot;" lemma="&amp;quot;" msd="XP" tag="&amp;quot;" in="13:pnct" out="">"</W>
<W gloss="Precisely" lemma="netop" msd="RGU" tag="RP" in="1:eval" out="">Netop</W>
<W gloss="because" lemma="fordi" msd="CS" tag="IN" in="11:cause" out="-1:eval|4:vobj">fordi</W>
<W gloss="we" lemma="vi" msd="PP1CPN-NU" tag="PRP" in="3:subj" out="">vi</W>
<W gloss="even" lemma="end" msd="RGU" tag="RP" in="1:eval" out="">end</W>
<W gloss="not" lemma="ikke" msd="RGU" tag="RP" in="1:neg" out="-1:eval">ikke</W>
<W gloss="do_have" lemma="have" msd="VADR=----A-" tag="VBD" in="-4:vobj" out="-3:subj|-1:neg|1:dobj|6:pnct">har</W>
<W gloss="a" lemma="en" msd="PI-NSU--U" tag="DT" in="-1:dobj" out="1:nobj">et</W>
<W gloss="germ" lemma="kim" msd="NCNSU==I" tag="NN" in="-1:nobj" out="1:pobj">kim</W>
<W gloss="of" lemma="af" msd="SP" tag="IN" in="-1:pobj" out="2:nobj">af</W>
<W gloss="civil" lemma="civil" msd="ANPNSU=IU" tag="JJ" in="1:attr" out="">civilt</W>
<W gloss="society" lemma="samfund" msd="NCNSU==I" tag="NN" in="-2:nobj" out="-1:attr">samfund</W>
<W gloss="," lemma="," msd="XP" tag="," in="-6:pnct" out="">,</W>
<W gloss="are" lemma="være" msd="VADA=----A-" tag="VBD" in="-15:qobj" out="-13:pnct|-11:cause|1:subj|2:preds|4:pnct">var</W>
<W gloss="we" lemma="vi" msd="PP1CPN-NU" tag="PRP" in="-1:subj" out="">vi</W>
<W gloss="against" lemma="imod" msd="SP" tag="IN" in="-2:preds" out="1:nobj">imod</W>
<W gloss="the_Duma" lemma="folkekongres" msd="NCCSU==D" tag="NN" in="-1:nobj" out="">Folkekongressen</W>
<W gloss="." lemma="." msd="XP" tag="." in="-4:pnct" out="">.</W>

<W gloss="Apart_from" lemma="bortset_fra" msd="SP" tag="IN" in="4:conc" out="1:nobj">Bortset_fra</W>
<W gloss="the_illusion" lemma="illusion" msd="NCCSU==D" tag="NN" in="-1:nobj" out="1:pobj">illusionen</W>
<W gloss="of" lemma="om" msd="SP" tag="IN" in="-1:pobj" out="1:nobj">om</W>
<W gloss="democracy" lemma="demokrati" msd="NCNSU==I" tag="NN" in="-1:nobj" out="">demokrati</W>
<W gloss="can" lemma="kunne" msd="VADA=----A-" tag="VBD" in="" out="-4:conc|1:subj|2:neg|3:vobj|6:pnct">kunne</W>
<W gloss="it" lemma="den" msd="PP3CSU-NU" tag="PRP" in="-1:subj|2:[subj]" out="">den</W>
<W gloss="not" lemma="ikke" msd="RGU" tag="RP" in="-2:neg" out="">ikke</W>
<W gloss="provide" lemma="give" msd="VAF-=----A-" tag="VB" in="-3:vobj" out="-2:[subj]|1:dobj">give</W>
<W gloss="something" lemma="nogen" msd="PI-NSU--U" tag="DT" in="-1:dobj" out="1:other">noget</W>
<W gloss="real" lemma="reel" msd="ANPNSU=IU" tag="JJ" in="-1:other" out="">reelt</W>
<W gloss="." lemma="." msd="XP" tag="." in="-6:pnct" out="">.</W>

<W gloss="It" lemma="det" msd="PP3NSU-NU" tag="PRP" in="1:dobj" out="">Det</W>
<W gloss="could" lemma="kunne" msd="VADA=----A-" tag="VBD" in="" out="-1:dobj|1:subj|2:neg|4:man|5:pnct">kunne</W>
<W gloss="the" lemma="den" msd="PP3CSU-NU" tag="PRP" in="-1:subj" out="">den</W>
<W gloss="not" lemma="ikke" msd="RGU" tag="RP" in="-2:neg" out="">ikke</W>
<W gloss="quite" lemma="hel" msd="ANP---=-R" tag="JJ" in="1:quant" out="">helt</W>
<W gloss="objectively" lemma="objektiv" msd="ANP---=-R" tag="JJ" in="-4:man" out="-1:quant">objektivt</W>
<W gloss="." lemma="." msd="XP" tag="." in="-5:pnct" out="">.</W>

<W gloss="This" lemma="det" msd="PP3NSU-NU" tag="PRP" in="1:subj" out="">Det</W>
<W gloss="was" lemma="være" msd="VADA=----A-" tag="VBD" in="" out="-1:subj|2:neg|3:preds|6:pnct">var</W>
<W gloss="even" lemma="slet" msd="RGU" tag="RP" in="1:quant" out="">slet</W>
<W gloss="not" lemma="ikke" msd="RGU" tag="RP" in="-2:neg" out="-1:quant">ikke</W>
<W gloss="på_grund_af" lemma="på_grund_af" msd="SP" tag="IN" in="-3:preds" out="1:nobj">på_grund_af</W>
<W gloss="its_life" lemma="apparat" msd="NCNSG==D" tag="NN" in="-1:nobj" out="1:possd">apparatets</W>
<W gloss="shackles" lemma="lænke" msd="NCCPU==I" tag="NNP" in="-1:possd" out="">lænker</W>
<W gloss="." lemma="." msd="XP" tag="." in="-6:pnct" out="">.</W>

<W gloss="Illusions" lemma="illusion" msd="NCCPU==I" tag="NNP" in="1:subj" out="">Illusioner</W>
<W gloss="are" lemma="være" msd="VADR=----A-" tag="VBD" in="" out="-1:subj|1:preds|2:pnct">er</W>
<W gloss="dangerous" lemma="farlig" msd="ANP[CN]PU=[DI]U" tag="JJ" in="-1:preds" out="">farlige</W>
<W gloss="." lemma="." msd="XP" tag="." in="-2:pnct" out="">.</W>

<W gloss="They" lemma="de" msd="PP3[CN]PN-NU" tag="PRP" in="1:subj|4:[subj]" out="">De</W>
<W gloss="breeds" lemma="føde" msd="VADR=----A-" tag="VBD" in="" out="-1:subj|1:dobj|3:conj|10:pnct|11:ref|14:rel|25:pnct|28:pnct">føder</W>
<W gloss="disappointment" lemma="skuffelse" msd="NCCPU==I" tag="NNP" in="-1:dobj" out="">skuffelser</W>
<W gloss="and" lemma="og" msd="CC" tag="CC" in="1:coord" out="">og</W>
<W gloss="lead" lemma="lede" msd="VADR=----A-" tag="VBD" in="-3:conj" out="-4:[subj]|-1:coord|1:time|2:pobj">leder</W>
<W gloss="ultimately" lemma="til_sidst" msd="RGU" tag="RP" in="-1:time" out="">til_sidst</W>
<W gloss="to" lemma="til" msd="SP" tag="IN" in="-2:pobj" out="1:nobj">til</W>
<W gloss="a" lemma="en" msd="PI-CSU--U" tag="DT" in="-1:nobj" out="1:nobj">en</W>
<W gloss="destabilization" lemma="destabilisering" msd="NCCSU==I" tag="NN" in="-1:nobj" out="1:pobj">destabilisering</W>
<W gloss="of" lemma="af" msd="SP" tag="IN" in="-1:pobj" out="1:nobj">af</W>
<W gloss="society" lemma="samfund" msd="NCNSU==D" tag="NN" in="-1:nobj" out="">samfundet</W>
<W gloss="," lemma="," msd="XP" tag="," in="-10:pnct" out="">,</W>
<W gloss="which" lemma="hvad" msd="PT-[CN]SU--U" tag="WDT" in="-11:ref|4:dobj" out="">hvad</W>
<W gloss="we" lemma="vi" msd="PP1CPN-NU" tag="PRP" in="2:subj|3:[subj]|6:[subj]|7:[subj]" out="">vi</W>
<W gloss="already" lemma="allerede" msd="RGU" tag="RP" in="1:time" out="">allerede</W>
<W gloss="have" lemma="have" msd="VADR=----A-" tag="VBD" in="-14:rel" out="-2:subj|-1:time|1:vobj|4:conj">har</W>
<W gloss="seen" lemma="se" msd="VAPA=S[CN]I[ARU]-U" tag="VBN" in="-1:vobj" out="-3:[subj]|-4:dobj">set</W>
<W gloss="and" lemma="og" msd="CC" tag="CC" in="2:coord" out="">og</W>
<W gloss="unfortunately" lemma="desværre" msd="RGU" tag="RP" in="1:eval" out="">desværre</W>
<W gloss="will" lemma="ville" msd="VADR=----A-" tag="VBD" in="-4:conj" out="-6:[subj]|-1:eval|-2:coord|1:vobj">vil</W>
<W gloss="come" lemma="komme" msd="VAF-=----A-" tag="VB" in="-1:vobj" out="-7:[subj]|1:pobj">komme</W>
<W gloss="in" lemma="til" msd="SP" tag="IN" in="-1:pobj" out="1:nobj">til</W>
<W gloss="to" lemma="at" msd="U=" tag="TO" in="-1:nobj" out="1:vobj">at</W>
<W gloss="see" lemma="se" msd="VAF-=----A-" tag="VB" in="-1:vobj" out="1:dobj">se</W>
<W gloss="more" lemma="meget" msd="ANC[CN]SU=IU" tag="JJR" in="-1:dobj" out="1:other">mere</W>
<W gloss="by" lemma="af" msd="SP" tag="IN" in="-1:other" out="">af</W>
<W gloss="." lemma="." msd="XP" tag="." in="-25:pnct" out="">.</W>

<W gloss="&amp;quot;" lemma="&amp;quot;" msd="XP" tag="&amp;quot;" in="-28:pnct" out="">"</W>
<W gloss="They" lemma="de" msd="PP3[CN]PN-NU" tag="PRP" in="1:subj" out="">De</W>
<W gloss="believe" lemma="mene" msd="VADR=----A-" tag="VBD" in="" out="-1:subj|1:pnct|2:dobj|9:pnct">mener</W>
<W gloss="," lemma="," msd="XP" tag="," in="-1:pnct" out="">,</W>
<W gloss="that" lemma="at" msd="CS" tag="IN" in="-2:dobj" out="2:vobj">at</W>
<W gloss="the_Duma" lemma="folkekongres" msd="NCCSU==D" tag="NN" in="1:subj|2:[subj]" out="">Folkekongressen</W>
<W gloss="should" lemma="skulle" msd="VADR=----A-" tag="VBD" in="-2:vobj" out="-1:subj|1:vobj">skal</W>
<W gloss="give" lemma="give" msd="VAF-=----A-" tag="VB" in="-1:vobj" out="-2:[subj]|1:iobj|3:dobj">give</W>
<W gloss="the_President" lemma="præsident" msd="NCCSU==D" tag="NN" in="-1:iobj" out="">præsidenten</W>
<W gloss="diktaroriske" lemma="diktaroriske" msd="XX" tag="FW" in="1:attr" out="">diktaroriske</W>
<W gloss="befølelser" lemma="befølelser" msd="XX" tag="FW" in="-3:dobj" out="-1:attr">befølelser</W>
<W gloss="." lemma="." msd="XP" tag="." in="-9:pnct" out="">.</W>"""


#Gloss
match_gloss = gloss.scanString(tekst1)
#pospremi u listu
lista_match_glosseva = []
nova_lista_gloss = []
for m in match_gloss:
	lista_match_glosseva.append(m[0])
for n in lista_match_glosseva:
	nova_lista_gloss.append(' '.join(n))
#PRINTANJE U JSON
lista_glosseva=json.dumps(nova_lista_gloss,indent =2)
print("Gloss: " + lista_glosseva)


#LEMME
match_lemma = lemma.scanString(tekst1)
lista_match_lemmi = []
nova_lista_lemmi = []
#POSPREMANJE U LISTU
for m in match_lemma:
	lista_match_lemmi.append(m[0])
for n in lista_match_lemmi:
	nova_lista_lemmi.append(' '.join(n))
json_lemme = json.dumps(nova_lista_lemmi,indent =2)
print("\nLemme: "+json_lemme)


#MSD
match_msd = msd.scanString(tekst1)
lista_match_msd = []
nova_lista_msd = []
#POSPREMANJE U LISTU
for m in match_msd:
	lista_match_msd.append(m[0])
for n in lista_match_msd:
	nova_lista_msd.append(' '.join(n))
json_msd = json.dumps(nova_lista_msd,indent =2)
print("\nMSD: "+json_msd)


#TAG
match_tag = tag.scanString(tekst1)
lista_match_tag = []
nova_lista_tag = []
#POSPREMANJE U LISTU
for m in match_tag:
	lista_match_tag.append(m[0])
for n in lista_match_tag:
	nova_lista_tag.append(' '.join(n))
json_tag = json.dumps(nova_lista_tag,indent =2)
print("\nTAG: "+json_tag)


#IN_
match_in_ = in_.scanString(tekst1)
lista_match_in_ = []
nova_lista_in_ = []
#POSPREMANJE U LISTU
for m in match_in_:
	lista_match_in_.append(m[0])
for n in lista_match_in_:
	nova_lista_in_.append(' '.join(n))
json_in_ = json.dumps(nova_lista_in_,indent =2)
print("\nIN: "+json_in_)


#IN_
match_out = out.scanString(tekst1)
lista_match_out = []
nova_lista_out = []
#POSPREMANJE U LISTU
for m in match_out:
	lista_match_out.append(m[0])
for n in lista_match_out:
	nova_lista_out.append(' '.join(n))
json_out = json.dumps(nova_lista_out,indent =2)
print("\nOUT: "+json_out)

datoteka = open("parsiranje.json","w")
datoteka.write("Gloss: " + lista_glosseva)
datoteka.write("\nLemme: " + json_lemme)
datoteka.write("\nMSD: " + json_msd)
datoteka.write("\nTAG: " + json_tag)
datoteka.write("\nin: " + json_in_)
datoteka.write("\nout: " + json_out)
datoteka.close()
	