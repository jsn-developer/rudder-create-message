/* Copyright 2021 SOLXYZ Co., Ltd. All Rights Reserved. */
package jp.co.solxyz.rudder.message;

public enum MessageCd {
  %{enums}

  String code;

  private MessageCd(String code) {
    this.code = code;
  }

  public String getCode() {
    return this.code;
  }
}