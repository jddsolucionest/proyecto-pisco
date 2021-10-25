import base64
script = b"""
IyEvdXNyL2Jpbi9weXRob24zDQojIC0qLSBjb2Rpbmc6IFVURi04DQoNCmltcG9ydCBvcw0KaW1w
b3J0IHRpbWUNCmltcG9ydCByZXF1ZXN0cw0KZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXAN
CmZyb20gcmVxdWVzdHMuc3RydWN0dXJlcyBpbXBvcnQgQ2FzZUluc2Vuc2l0aXZlRGljdA0KZnJv
bSBjb2xvcmFtYSBpbXBvcnQgRm9yZSwgaW5pdA0KaW5pdCgpDQoNCiNjb2xvcmVzDQp2ZXJkZSA9
IEZvcmUuR1JFRU4NCmx2ZXJkZSA9IEZvcmUuTElHSFRHUkVFTl9FWA0Kcm9qbyA9IEZvcmUuUkVE
DQpscm9qbyA9IEZvcmUuTElHSFRSRURfRVgNCmFtYXJpbGxvID0gRm9yZS5ZRUxMT1cNCmJsYW5j
byA9IEZvcmUuV0hJVEUNCmN5YW4gPSBGb3JlLkNZQU4NCnZpb2xldGEgPSBGb3JlLk1BR0VOVEEN
CmF6dWwgPSBGb3JlLkJMVUUNCmxhenVsID0gRm9yZS5MSUdIVEJMVUVfRVgNCg0KIyMjIyMjIyMj
IyMjIyMjIyMjIyBGVU5DSU9ORVMgREUgTEEgSEVSUkFNSUVOVEENCiMgc2lzdGVtYSBkZSBudW1l
cm9zIGRlIGRuaQ0KZGVmIGNvbnN1bHRhZG5pKCk6DQogICAgZG5pID0gaW5wdXQoIkVzY3JpYmUg
ZWwgZG5pOiAiKQ0KICAgIHVybCA9IGYiaHR0cHM6Ly9kbmlydWMuYXBpc3BlcnUuY29tL2FwaS92
MS9kbmkve2RuaX0/dG9rZW49ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5
SmxiV0ZwYkNJNkltZHlZV1I1TXpsMVgyNHlPVEZwUUc1aFpuaHZMbU52YlNKOS5jbDVLUXpzWGFS
dUx1d0VVV05KRExYX1poMlJfSGtCc245X1lFUDRrZWlvIg0KICAgIGRhdGEgPSByZXF1ZXN0cy5n
ZXQodXJsKQ0KICAgIHJlc3B1ZXN0YSA9IGRhdGEuanNvbigpDQogICAgbmRuaSA9IHJlc3B1ZXN0
YVsnZG5pJ10NCiAgICBpZiBuZG5pID09ICcnOg0KICAgICAgICBwcmludCgiTlVNRVJPIERFIERO
SSBOTyBFTkNPTlRSQURPIikNCiAgICBlbGlmIG5kbmkgaXMgTm9uZToNCiAgICAgICAgcHJpbnQo
Ik5VTUVSTyBERSBETkkgTk8gRU5DT05UUkFETyIpDQogICAgZWxzZToNCiAgICAgICAgbmFtZSA9
IHJlc3B1ZXN0YVsnbm9tYnJlcyddDQogICAgICAgIGFwZWxsaWRvcCA9IHJlc3B1ZXN0YVsnYXBl
bGxpZG9QYXRlcm5vJ10NCiAgICAgICAgYXBlbGxpZG9tID0gcmVzcHVlc3RhWydhcGVsbGlkb01h
dGVybm8nXQ0KICAgICAgICBjb2RpZ292ID0gcmVzcHVlc3RhWydjb2RWZXJpZmljYSddDQogICAg
ICAgIHByaW50KGYie3ZlcmRlfU5PTUJSRTp7YmxhbmNvfSB7bmFtZX1cbnt2ZXJkZX1BUEVMTElE
TyBQQVRFUk5POntibGFuY299IHthcGVsbGlkb3B9XG57dmVyZGV9QVBFTExJRE8gTUFURVJOTzp7
YmxhbmNvfSB7YXBlbGxpZG9tfVxue3ZlcmRlfUROSTp7YmxhbmNvfSB7ZG5pfVxue3ZlcmRlfUPD
k0RJR086e2JsYW5jb30ge2NvZGlnb3Z9XG4iKQ0KDQojc2lzdGVtYSBkZSB2ZXJpZmljYWNpb24g
ZGUgcnVjDQpkZWYgY29uc3VsdGFydWMoKToNCiAgICB0b2tlbiA9ICc/dG9rZW49ZXlKMGVYQWlP
aUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SmxiV0ZwYkNJNkltZHlZV1I1TXpsMVgyNHlP
VEZwUUc1aFpuaHZMbU52YlNKOS5jbDVLUXpzWGFSdUx1d0VVV05KRExYX1poMlJfSGtCc245X1lF
UDRrZWlvJw0KICAgIHJ1Y2tpID0gaW5wdXQoIlJVQyA+PiAiKQ0KICAgIHJlc3BvbnNlID0gcmVx
dWVzdHMuZ2V0KCJodHRwczovL2RuaXJ1Yy5hcGlzcGVydS5jb20vYXBpL3YxL3J1Yy8iICtydWNr
aSArdG9rZW4pDQogICAgZm9yIGtleSwgdmFsdWUgaW4gcmVzcG9uc2UuanNvbigpLml0ZW1zKCk6
DQogICAgICAgIHByaW50KCJbLV0gJXM6ICVzIiAlIChrZXksIHZhbHVlKSkNCg0KIyBzaXN0ZW1h
IGRlIGJ1c3F1ZWRhIGRlIGRpcmVjY2lvbiBkZSBjYXNhDQpkZWYgZGlyZWNjaW9uX2Nhc2EoKToN
CiAgICBudW1lcm8gPSBpbnB1dCgiSU5HUkVTQSBETkk6ICIpDQogICAgdXJsID0gZiJodHRwOi8v
Y3BlLmZhY3R1cmFwZXJ1YW5hLmNvbS9jbGllbnRlL2FwaXN1dHJhbl9kbmkve251bWVyb30iDQog
ICAgcmVzcCA9IHJlcXVlc3RzLmdldCh1cmwpDQogICAgdGV4dG8gPSByZXNwLnRleHQNCiAgICBu
ZXdfZG5pID0gdGV4dG9bMzpdDQogICAgbmV3X2RuaTIgPSBuZXdfZG5pWzotM10NCiAgICBjb3J0
ZSA9IG5ld19kbmkyLnNwbGl0KHNlcD0nLCcpDQogICAgZm9yIGkgaW4gY29ydGU6DQogICAgICAg
IHByaW50KCI+PiAiK2kpDQoNCiMgc2lzdGVtYSBkZSBidXNxdWVkYSBkZSBuw7ptZXJvcyB0ZWxl
ZsOzbmljb3MNCmRlZiBjb25zdWx0YWluZGl2aWR1YWwoKToNCiAgICBudW1lcm90ZWxlZm9uaWNv
ID0gaW5wdXQoIlsrXSBFU0NSSUJFIEVMIE7Dmk1FUk8gVEVMRUbDk05JQ086ICIpDQogICAgdXJs
MSA9IGYiaHR0cDovL2FwaWxheWVyLm5ldC9hcGkvdmFsaWRhdGU/YWNjZXNzX2tleT1hMzRkOTdm
MDNlNTFlOTkxZDY2OTliOWRlMGI4Njk0YyZudW1iZXI9e251bWVyb3RlbGVmb25pY299JmNvdW50
cnlfY29kZSZmb3JtYXQ9MSINCiAgICB1cmwyID0gZiJodHRwczovL3Bob25ldmFsaWRhdGlvbi5h
YnN0cmFjdGFwaS5jb20vdjEvP2FwaV9rZXk9NDlmNGZlOTgyYTFiNGY1Y2FjZGRlMDM2MDgxNjFj
ZGQmcGhvbmU9e251bWVyb3RlbGVmb25pY299Ig0KDQogICAgZGF0YTEgPSByZXF1ZXN0cy5nZXQo
ZiJ7dXJsMX0iKQ0KICAgIGRhdGEyID0gcmVxdWVzdHMuZ2V0KGYie3VybDJ9IikNCg0KICAgIGRh
dGFKc29uMSA9IGRhdGExLmpzb24oKQ0KICAgIGRhdGFKc29uMiA9IGRhdGEyLmpzb24oKQ0KDQog
ICAgZXhpc3Rlb25vID0gZGF0YUpzb24xWydsb2NhbF9mb3JtYXQnXQ0KDQogICAgICAgICMgZGF0
b3MgdXJsIG51bWVybyAxDQogICAgdmFsaWRhciA9IGRhdGFKc29uMVsndmFsaWQnXQ0KICAgIHBy
ZWZpam8gPSBkYXRhSnNvbjFbJ2NvdW50cnlfcHJlZml4J10NCiAgICBjb2RpZ28gPSBkYXRhSnNv
bjFbJ2NvdW50cnlfY29kZSddDQogICAgY29kaWdvX3BhaXMgPSBkYXRhSnNvbjFbJ2NvdW50cnlf
bmFtZSddDQogICAgbG9jYWxpemFjaW9uID0gZGF0YUpzb24xWydsb2NhdGlvbiddDQogICAgICAg
ICNkYXRvcyB1cmwgbnVtZXJvIDINCiAgICBmb3JtYXRvX2xvY2FsX3BhaXMgPSBkYXRhSnNvbjJb
J2Zvcm1hdCddWydsb2NhbCddDQogICAgY2FycmlsID0gZGF0YUpzb24yWydjYXJyaWVyJ10NCiAg
ICBpZiBleGlzdGVvbm8gPT0gJyc6DQogICAgICAgIHByaW50KGYie2xyb2pvfU5PIEVYSVNURSAi
KQ0KICAgIGVsaWYgZXhpc3Rlb25vIGlzIE5vbmU6DQogICAgICAgIHByaW50KGYie2xyb2pvfU5P
IEVYSVNURSAiKQ0KICAgIGVsc2U6DQogICAgICAgIHByaW50KGYie2F6dWx9RVMgVkFMSURPID8g
OntibGFuY299IHt2YWxpZGFyfVxue2F6dWx9UFJFRklKTyA6e2JsYW5jb30ge3ByZWZpam99XG57
YXp1bH1GT1JNQVRPIExPQ0FMIDp7YmxhbmNvfSB7Zm9ybWF0b19sb2NhbF9wYWlzfVxue2F6dWx9
Q09ESUdPIERFTCBQQUlTIDp7YmxhbmNvfSB7Y29kaWdvfVxue2F6dWx9UEFJUyA6e2JsYW5jb30g
e2NvZGlnb19wYWlzfVxue2F6dWx9TE9DQUxJWkFDScOTTiA6e2JsYW5jb30ge2xvY2FsaXphY2lv
bn1cbnthenVsfUNPTVBBw5FJQSA6e2JsYW5jb30ge2NhcnJpbH1cbiIpDQoNCiMgY29uc3VsdGEg
ZGUgbm9tYnJlcyB5IGFwZWxsaWRvcyBwb3IgZG5pDQpkZWYgY29uc3VsdGFfcG9yX25vbWJyZXMo
KToNCiAgICBuYW1lID0gaW5wdXQoIkVTQ1JJQkUgRUwgTk9NQlJFOiAiKQ0KICAgIGFwZWxsaWRv
cCA9IGlucHV0KCJFU0NSSUJFIEVMIEFQRUxMSURPIFBBVEVSTk86ICIpDQogICAgYXBlbGxpZG9t
ID0gaW5wdXQoIkVTQ1JJQkUgRUwgQVBFTExJRE8gTUFURVJOTzogIikNCiAgICB1cmwgPSAiaHR0
cHM6Ly9idXNjYXJkbmkueHl6L2J1c2NhZG9yL2VqZW1wbG9fYWpheF9wcm9jZXNvLnBocCINCiAg
ICBoZWFkZXJzID0gQ2FzZUluc2Vuc2l0aXZlRGljdCgpDQogICAgaGVhZGVyc1siQ29udGVudC1U
eXBlIl0gPSAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIg0KICAgIGRhdGEgPSBm
IkFQRV9QQVQ9e2FwZWxsaWRvcH0mQVBFX01BVD17YXBlbGxpZG9tfSZOT01CUkVTPXtuYW1lfSIN
CiAgICByZXNwID0gcmVxdWVzdHMucG9zdCh1cmwsIGhlYWRlcnM9aGVhZGVycywgZGF0YT1kYXRh
KQ0KICAgIHRleHQgPSByZXNwLnRleHQNCiAgICBzb3VwID0gQmVhdXRpZnVsU291cCh0ZXh0LCAi
bHhtbCIpDQogICAgdGV4dDIgPSBzb3VwLmdldF90ZXh0KCkNCiAgICBuZXdfYiA9IHRleHQyWzEz
MTpdDQogICAgY2hhcmFjdGVycyA9ICJ2ZXIiDQogICAgc3RyaW5nID0gJycuam9pbiggeCBmb3Ig
eCBpbiBuZXdfYiBpZiB4IG5vdCBpbiBjaGFyYWN0ZXJzKQ0KICAgIHByaW50KHN0cmluZykNCg0K
DQpkZWYgcG9ydGFkYSgpOg0KICAgIHByaW50KGYiIiJ7dmlvbGV0YX0gICAgICAgLiAgICAgICAu
ICAgICAgICAuICAgIC4gICAgICAgLiAgICAgLiANCiDilojilojilojilojilojilojilZcg4paI
4paI4pWX4paI4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDiloji
lojilojilojilojilojilZcgLiAgLiAgIC4gICAuICAuICAgLiAuICAgLg0KIOKWiOKWiOKVlOKV
kOKVkOKWiOKWiOKVl+KWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKVkOKVkOKVneKWiOKWiOKVlOKV
kOKVkOKVkOKVkOKVneKWiOKWiOKVlOKVkOKWiOKWiOKWiOKWiOKVlyAg4paE4paA4paA4paA4paA
4paA4paEe3Zpb2xldGF9LiAgLiAgLiAgDQog4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI
4pWR4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWRICAgICDilojilojilZHilojiloji
lZTilojilojilZEg4paQ4paR4paE4paR4paR4paR4paE4paR4paMe3Zpb2xldGF9LiAgLiAgIC4g
DQog4paI4paI4pWU4pWQ4pWQ4pWQ4pWdIOKWiOKWiOKVkeKVmuKVkOKVkOKVkOKVkOKWiOKWiOKV
keKWiOKWiOKVkSAgICAg4paI4paI4paI4paI4pWU4pWd4paI4paI4pWRIOKWkOKWkeKWgOKWgOKW
keKWgOKWgOKWkeKWjHt2aW9sZXRhfSAgLiAgIC4gICAuIA0KIOKWiOKWiOKVkSAgICAg4paI4paI
4pWR4paI4paI4paI4paI4paI4paI4paI4pWR4pWa4paI4paI4paI4paI4paI4paI4pWX4pWa4paI
4paI4paI4paI4paI4paI4pWU4pWdICDiloDiloTilpHilZDilpHiloTiloB7dmlvbGV0YX0gLiAg
IC4gICAgIA0KIOKVmuKVkOKVnSAgICAg4pWa4pWQ4pWd4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWd
IOKVmuKVkOKVkOKVkOKVkOKVkOKVnSDilZrilZDilZDilZDilZDilZDilZ0gLiDilpDilpHiloDi
loTiloDilpHilowge3Zpb2xldGF9ICAgIC4gLiAgIA0KIHt2ZXJkZX1QUk9HUkFNQURPIFBPUiBE
NFZJRC4wICAgICAgICAgICAgICAgICAge2N5YW59VmVyc2nDs24gMi4xIC4gICAuDQoge2x2ZXJk
ZX3ilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi
lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDi
lZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZANCiB7
bHJvam99SU5TVEFHUkFNOiB7YmxhbmNvfWQ0dmlkLjBkYXkNCiB7YmxhbmNvfUdJVEhVQjp7Ymxh
bmNvfSBodHRwczovL2dpdGh1Yi5jb20vTW9ua2V5LWhrNA0KIHthenVsfVRFTEVHUkFNOntibGFu
Y299IG1oazRfMA0KIHtsYXp1bH1ET05BQ0lPTkVTOntibGFuY299IGh0dHBzOi8vd3d3LnBheXBh
bC5jb20vcGF5cGFsbWUvZGF2aWRoazQNCiB7bHZlcmRlfeKVkOKVkOKVkOKVkOKVkOKVkOKVkOKV
kOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKV
kOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKV
kOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkA0KICAgICIiIikNCiAgICB0aW1lLnNsZWVwKDAu
NSkNCg0KZGVmIG1lbnVfYXl1ZGEoKToNCiAgICBwcmludCgiIiINCiBNRU5VIERFIE9QQ0lPTkVT
IC0gUFJPWUVDVE8gUElTQzANCiDDmkxUSU1BIEFDVFVBTElaQUNJw5NOIDIwLzEwLzIwMjEgDQog
DQogIENPTUFORE8gICAgICAgICAgICAgICAgICBJTkZPUk1BQ0nDk04gDQoNCiBbIGRuaSBdIE1v
c3RhciBOb21icmVzIHkgQXBlbGxpZG9zIGRlIHVuIG7Dum1lcm8gZGUgZG5pIHB1ZWRlIHNlciAr
MTggJi0xOA0KIFsgY2FzYSBdIGRpcmVjY2nDs24gZGUgY2FzYSBkb25kZSB2aXZlIHVuYSBwZXJz
b25hIHBvciBzdSBuwrAgZGUgZG5pDQogWyBydWMgXSBEYXRvcyBkZSB1bmEgUlVDLCB0aXR1bGFy
LCByYXrDs24gc29jaWFsLCBldGMNCiBbIG51bWVybyBdIEluZm9ybWFjacOzbiBkZSB1biBuw7pt
ZXJvIHRlbGVmw7NuaWNvIA0KDQogRWwgc2NyaXB0IHNlIHZhIGEgYWN0dWFsaXphciB0b2RvcyBs
b3MgbWVzZXMgeSBzZSB2YSBhIGHDsWFkaXIgbcOhcyBvcGNpb25lcy4gDQogICAgIiIiKSAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0KDQpkZWYgZWxlY2Npb24oKToNCiAgICBv
cGMgPSBpbnB1dChmInt2ZXJkZX1bcGlzY29Acm9vdF0+PiAiKQ0KICAgIGlmIG9wYyA9PSAiZG5p
IjoNCiAgICAgICAgY29uc3VsdGFkbmkoKQ0KICAgICAgICBlbGVjY2lvbigpDQogICAgZWxpZiBv
cGMgPT0gImhlbHAiOg0KICAgICAgICBtZW51X2F5dWRhKCkNCiAgICAgICAgZWxlY2Npb24oKQ0K
ICAgIGVsaWYgb3BjID09ICJheXVkYSI6DQogICAgICAgIG1lbnVfYXl1ZGEoKQ0KICAgICAgICBl
bGVjY2lvbigpDQogICAgZWxpZiBvcGMgPT0gIj8iOg0KICAgICAgICBtZW51X2F5dWRhKCkNCiAg
ICAgICAgZWxlY2Npb24oKQ0KICAgIGVsaWYgb3BjID09ICJjYXNhIjoNCiAgICAgICAgZGlyZWNj
aW9uX2Nhc2EoKQ0KICAgICAgICBlbGVjY2lvbigpDQogICAgZWxpZiBvcGMgPT0gInJ1YyI6DQog
ICAgICAgIGNvbnN1bHRhcnVjKCkNCiAgICAgICAgZWxlY2Npb24oKQ0KICAgIGVsaWYgb3BjID09
ICJudW1lcm8iOg0KICAgICAgICBjb25zdWx0YWluZGl2aWR1YWwoKQ0KICAgICAgICBlbGVjY2lv
bigpDQogICAgZWxpZiBvcGMgPT0gImJ1c2NhciI6DQogICAgICAgIGNvbnN1bHRhX3Bvcl9ub21i
cmVzKCkNCiAgICAgICAgZWxlY2Npb24oKQ0KICAgIGVsaWYgb3BjID09ICJjbGVhciI6DQogICAg
ICAgIG9zLnN5c3RlbSgiY2xlYXIiKQ0KICAgICAgICBwb3J0YWRhKCkNCiAgICAgICAgZWxlY2Np
b24oKQ0KICAgIGVsaWYgb3BjID09ICJjbHMiOg0KICAgICAgICBvcy5zeXN0ZW0oImNscyIpDQog
ICAgICAgIHBvcnRhZGEoKQ0KICAgICAgICBlbGVjY2lvbigpICAgIA0KICAgIGVsc2U6DQogICAg
ICAgIHByaW50KCIiIlwwMzNbMzNtDQogICAgRVJST1IgNDA0IE9QQ0nDk04gSU5DT1JSRUNUQSB4
X3ggDQogICAgICAgICIiIikNCiAgICAgICAgZWxlY2Npb24oKQ0KICAgIA0KIyBpbmljaW8gZGUg
dG9vbA0KIyAyMi0wOC0yMDIxIGdhYWFhIGphamFqYWphamphamFqYQ0KDQpwb3J0YWRhKCkNCmVs
ZWNjaW9uKCkNCg==
"""
exec(base64.b64decode(script))
