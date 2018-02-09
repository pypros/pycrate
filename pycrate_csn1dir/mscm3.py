# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.3
# *
# * Copyright 2017. Benoit Michau. ANSSI.
# *
# * This program is free software; you can redistribute it and/or
# * modify it under the terms of the GNU General Public License
# * as published by the Free Software Foundation; either version 2
# * of the License, or (at your option) any later version.
# * 
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# * 
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# * 02110-1301, USA.
# *
# *--------------------------------------------------------
# * File Name : pycrate_csndir/mscm3.py
# * Created : 2017-06-15
# * Authors : Benoit Michau 
# *--------------------------------------------------------
#*/

# Mobile Station Classmark 3
# TS 24.008, 10.5.1.7

# code automatically generated by pycrate_csn1
# change object type with type=T_BYTES
# add dict for value interpretation with dict={...}

from pycrate_csn1.csnobj import *

spare_bit = CSN1Bit(name='spare_bit')
Spare_bit = spare_bit
Spare_Bit = spare_bit
spare_bits = CSN1Bit(name='spare_bits', num=-1)
Spare_bits = spare_bits
Spare_Bits = spare_bits

MS_Positioning_Method_Capability = CSN1Bit(name='MS_Positioning_Method_Capability', root=True, bit=5)

R_Support = CSN1Bit(name='R_Support', root=True, bit=3)

ECSD_Multi_Slot_Capability = CSN1Bit(name='ECSD_Multi_Slot_Capability', root=True, bit=5)

_8_PSK_Struct = CSN1List(name='_8_PSK_Struct', root=True, list=[
  CSN1Bit(name='Modulation_Capability'),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Bit(name='_8_PSK_RF_Power_Capability_1', bit=2)]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Bit(name='_8_PSK_RF_Power_Capability_2', bit=2)]),
    '0': ('', [])})])

Single_Band_Support = CSN1Bit(name='Single_Band_Support', root=True, bit=4)

MS_Measurement_capability = CSN1List(name='MS_Measurement_capability', root=True, list=[
  CSN1Bit(name='SMS_VALUE', bit=4),
  CSN1Bit(name='SM_VALUE', bit=4)])

HSCSD_Multi_Slot_Capability = CSN1Bit(name='HSCSD_Multi_Slot_Capability', root=True, bit=5)

A5_bits = CSN1List(name='A5_bits', root=True, list=[
  CSN1Bit(name='A5_7'),
  CSN1Bit(name='A5_6'),
  CSN1Bit(name='A5_5'),
  CSN1Bit(name='A5_4')])

Classmark_3_Value_part = CSN1List(name='Classmark_3_Value_part', root=True, list=[
  CSN1Ref(obj=spare_bit),
  CSN1Alt(klen=3, alt={
    '100': ('Multiband supported', [
    CSN1Ref(obj=A5_bits),
    CSN1Ref(obj=spare_bit, num=4),
    CSN1Bit(name='Associated_Radio_Capability_1', bit=4)]),
    '001': ('Multiband supported', [
    CSN1Ref(obj=A5_bits),
    CSN1Ref(obj=spare_bit, num=4),
    CSN1Bit(name='Associated_Radio_Capability_1', bit=4)]),
    '010': ('Multiband supported', [
    CSN1Ref(obj=A5_bits),
    CSN1Ref(obj=spare_bit, num=4),
    CSN1Bit(name='Associated_Radio_Capability_1', bit=4)]),
    '000': ('Multiband supported', [
    CSN1Ref(obj=A5_bits)]),
    '110': ('Multiband supported', [
    CSN1Ref(obj=A5_bits),
    CSN1Bit(name='Associated_Radio_Capability_2', bit=4),
    CSN1Bit(name='Associated_Radio_Capability_1', bit=4)]),
    '101': ('Multiband supported', [
    CSN1Ref(obj=A5_bits),
    CSN1Bit(name='Associated_Radio_Capability_2', bit=4),
    CSN1Bit(name='Associated_Radio_Capability_1', bit=4)])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Ref(obj=R_Support)]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Ref(obj=HSCSD_Multi_Slot_Capability)]),
    '0': ('', [])}),
  CSN1Bit(name='UCS2_treatment'),
  CSN1Bit(name='Extended_Measurement_Capability'),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Ref(obj=MS_Measurement_capability)]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Ref(obj=MS_Positioning_Method_Capability)]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Ref(obj=ECSD_Multi_Slot_Capability)]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Ref(obj=_8_PSK_Struct)]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Alt(name='GSM_400_Bands_Supported', klen=2, alt={
      '01': ('', []),
      '10': ('', []),
      '11': ('', [])}),
    CSN1Bit(name='GSM_400_Associated_Radio_Capability', bit=4)]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Bit(name='GSM_850_Associated_Radio_Capability', bit=4)]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Bit(name='GSM_1900_Associated_Radio_Capability', bit=4)]),
    '0': ('', [])}),
  CSN1Bit(name='UMTS_FDD_Radio_Access_Technology_Capability'),
  CSN1Bit(name='UMTS_3_84_Mcps_TDD_Radio_Access_Technology_Capability'),
  CSN1Bit(name='CDMA_2000_Radio_Access_Technology_Capability'),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Bit(name='DTM_GPRS_Multi_Slot_Class', bit=2),
    CSN1Bit(name='Single_Slot_DTM'),
    CSN1Alt(alt={
      '1': ('', [
      CSN1Bit(name='DTM_EGPRS_Multi_Slot_Class', bit=2)]),
      '0': ('', [])})]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Ref(obj=Single_Band_Support)]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Bit(name='GSM_750_Associated_Radio_Capability', bit=4)]),
    '0': ('', [])}),
  CSN1Bit(name='UMTS_1_28_Mcps_TDD_Radio_Access_Technology_Capability'),
  CSN1Bit(name='GERAN_Feature_Package_1'),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Bit(name='Extended_DTM_GPRS_Multi_Slot_Class', bit=2),
    CSN1Bit(name='Extended_DTM_EGPRS_Multi_Slot_Class', bit=2)]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Bit(name='High_Multislot_Capability', bit=2)]),
    '0': ('', [])}),
  CSN1Val(name='', val='0'),
  CSN1Bit(name='GERAN_Feature_Package_2'),
  CSN1Bit(name='GMSK_Multislot_Power_Profile', bit=2),
  CSN1Bit(name='_8_PSK_Multislot_Power_Profile', bit=2),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Alt(name='T_GSM_400_Bands_Supported', klen=2, alt={
      '01': ('', []),
      '10': ('', []),
      '11': ('', [])}),
    CSN1Bit(name='T_GSM_400_Associated_Radio_Capability', bit=4)]),
    '0': ('', [])}),
  CSN1Val(name='', val='0'),
  CSN1Bit(name='Downlink_Advanced_Receiver_Performance', bit=2),
  CSN1Bit(name='DTM_Enhancements_Capability'),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Bit(name='DTM_GPRS_High_Multi_Slot_Class', bit=3),
    CSN1Bit(name='Offset_required'),
    CSN1Alt(alt={
      '1': ('', [
      CSN1Bit(name='DTM_EGPRS_High_Multi_Slot_Class', bit=3)]),
      '0': ('', [])})]),
    '0': ('', [])}),
  CSN1Bit(name='Repeated_ACCH_Capability'),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Bit(name='GSM_710_Associated_Radio_Capability', bit=4)]),
    '0': ('', [])}),
  CSN1Alt(alt={
    '1': ('', [
    CSN1Bit(name='T_GSM_810_Associated_Radio_Capability', bit=4)]),
    '0': ('', [])}),
  CSN1Bit(name='Ciphering_Mode_Setting_Capability'),
  CSN1Bit(name='Additional_Positioning_Capabilities'),
  CSN1Bit(name='E_UTRA_FDD_support'),
  CSN1Bit(name='E_UTRA_TDD_support'),
  CSN1Bit(name='E_UTRA_Measurement_and_Reporting_support'),
  CSN1Bit(name='Priority_based_reselection_support'),
  CSN1Bit(name='UTRA_CSG_Cells_Reporting'),
  CSN1Bit(name='VAMOS_Level', bit=2),
  CSN1Bit(name='TIGHTER_Capability', bit=2),
  CSN1Bit(name='Selective_Ciphering_of_Downlink_SACCH'),
  CSN1Bit(name='CS_to_PS_SRVCC_from_GERAN_to_UTRA', bit=2),
  CSN1Bit(name='CS_to_PS_SRVCC_from_GERAN_to_E_UTRA', bit=2),
  CSN1Bit(name='GERAN_Network_Sharing_support'),
  CSN1Bit(name='E_UTRA_Wideband_RSRQ_measurements_support'),
  CSN1Bit(name='ER_Band_Support'),
  CSN1Bit(name='UTRA_Multiple_Frequency_Band_Indicators_support'),
  CSN1Bit(name='E_UTRA_Multiple_Frequency_Band_Indicators_support'),
  CSN1Bit(name='Extended_TSC_Set_Capability_support'),
  CSN1Bit(name='Extended_EARFCN_value_range'),
  CSN1Ref(obj=spare_bits)])

