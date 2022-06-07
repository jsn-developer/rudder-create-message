/* Copyright 2021 SOLXYZ Co., Ltd. All Rights Reserved. */
package jp.co.solxyz.rudder.message;

public enum MessageCd {
  R_SQ_0001_E("R-SQ-0001-E"),
  R_SD_0002_E("R-SD-0002-E"),
  R_SD_0003_E("R-SD-0003-E");

  String code;

  private MessageCd(String code) {
    this.code = code;
  }

  public String getCode() {
    return this.code;
  }
}