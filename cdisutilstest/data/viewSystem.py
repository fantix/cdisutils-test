values = {
    "itemType=account&id=0": {
        "status_code": "200",
        "text": {
            "responseData": {
                "accessPools": [],
                "accounts": [],
                "cabinets": [],
                "devices": [],
                "eventCategories": [],
                "fileServerPools": [],
                "fileSystems": [],
                "groups": [],
                "metadataClusters": [],
                "mirrors": [],
                "networkNodes": [],
                "shares": [],
                "sites": [],
                "storagePoolGroups": [],
                "storagePools": [],
                "tags": [],
                "vaults": []
            },
            "responseHeader": {
                "now": 1492026962655,
                "requestId": "WO6GUgoQgF4AAAZwypkAAAC4",
                "status": "ok"
            },
            "responseStatus": "ok"
        }
    },
    "itemType=account&id=72": {
        "status_code": "200",
        "text": {
            "responseData": {
                "accessPools": [],
                "accounts": [
                    {
                        "accessKeys": [
                            {
                                "accessKeyId": "XXXXXXXXXXXXXXXXXXXXXX",
                                "creationDate": "Thu, 30 Mar 2017 15:26:07 +0000",
                                "secretAccessKey": "YYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
                            }
                        ],
                        "creationDate": "Thu, 30 Mar 2017 15:24:17 +0000",
                        "email": None,
                        "enabled": True,
                        "id": 72,
                        "keystoneDomain": None,
                        "managerLocale": None,
                        "name": "ResponseSuccess",
                        "organization": 1,
                        "privateAccountEnabled": False,
                        "roles": [
                            {
                                "role": "admin"
                            },
                            {
                                "role": "securityAdmin"
                            },
                            {
                                "role": "operator"
                            },
                            {
                                "role": "vaultProvisioner"
                            },
                            {
                                "role": "vaultUser",
                                "vaultPermissions": [
                                    {
                                        "permission": "owner",
                                        "vault": 274
                                    }
                                ]
                            }
                        ],
                        "timezone": None,
                        "type": "local",
                        "username": "testUsername",
                        "uuid": "AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEEE"
                    }
                ],
                "cabinets": [],
                "devices": [],
                "eventCategories": [],
                "fileServerPools": [],
                "fileSystems": [],
                "groups": [],
                "metadataClusters": [],
                "mirrors": [],
                "networkNodes": [],
                "shares": [],
                "sites": [],
                "storagePoolGroups": [],
                "storagePools": [],
                "tags": [],
                "vaults": []
            },
            "responseHeader": {
                "now": 1491594577080,
                "requestId": "WOftUAoQgF4AAHYXwR8AAACc",
                "status": "ok"
            },
            "responseStatus": "ok"
        }
    },    
    "itemType=account&id=12": {
        "status_code": "200",
        "text": {
            "responseData": {
                "accessPools": [],
                "accounts": [
                    {
                        "accessKeys": [
                            {
                                "accessKeyId": "YYYYYYYYYYYYYYY",
                                "creationDate": "Thu, 30 Mar 2017 15:26:07 +0000",
                                "secretAccessKey": "YYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
                            }
                        ],
                        "creationDate": "Thu, 30 Mar 2017 15:24:17 +0000",
                        "email": None,
                        "enabled": True,
                        "id": 12,
                        "keystoneDomain": None,
                        "managerLocale": None,
                        "name": "KeyPairErrorUser",
                        "organization": 1,
                        "privateAccountEnabled": False,
                        "roles": [
                            {
                                "role": "admin"
                            },
                            {
                                "role": "securityAdmin"
                            },
                            {
                                "role": "operator"
                            },
                            {
                                "role": "vaultProvisioner"
                            },
                            {
                                "role": "vaultUser",
                                "vaultPermissions": [
                                    {
                                        "permission": "owner",
                                        "vault": 274
                                    }
                                ]
                            }
                        ],
                        "timezone": None,
                        "type": "local",
                        "username": "testUsername",
                        "uuid": "AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEEE"
                    }
                ],
                "cabinets": [],
                "devices": [],
                "eventCategories": [],
                "fileServerPools": [],
                "fileSystems": [],
                "groups": [],
                "metadataClusters": [],
                "mirrors": [],
                "networkNodes": [],
                "shares": [],
                "sites": [],
                "storagePoolGroups": [],
                "storagePools": [],
                "tags": [],
                "vaults": []
            },
            "responseHeader": {
                "now": 1491594577080,
                "requestId": "WOftUAoQgF4AAHYXwR8AAACc",
                "status": "ok"
            },
            "responseStatus": "ok"
        }
    },
    "itemType=vault&id=274": {
        "status_code": 200,
        "text": {
            "responseData": {
                "accessPools": [],
                "accounts": [],
                "cabinets": [],
                "devices": [],
                "eventCategories": [],
                "fileServerPools": [],
                "fileSystems": [],
                "groups": [],
                "metadataClusters": [],
                "mirrors": [],
                "networkNodes": [],
                "shares": [],
                "sites": [],
                "storagePoolGroups": [],
                "storagePools": [],
                "tags": [],
                "vaults": [
                    {
                        "accessHealth": "all",
                        "accessPermissions": [
                            {
                                "permission": "readOnly",
                                "principal": {
                                    "id": 95,
                                    "type": "account"
                                },
                                "role": "vaultUser"
                            },
                            {
                                "permission": "owner",
                                "principal": {
                                    "id": 12,
                                    "type": "account"
                                },
                                "role": "vaultUser"
                            }
                        ],
                        "accessPools": [
                            1
                        ],
                        "alertLevel": 8,
                        "allotment": 1,
                        "allowedIps": [],
                        "anonymousAccessPermission": "disabled",
                        "creationDate": "Mon, 22 Aug 2016 14:18:30 +0000",
                        "deleteRestricted": False,
                        "description": "this is a test Vaul",
                        "extentEnabled": False,
                        "externalAccessHost": None,
                        "fileSystem": None,
                        "generations": [
                            {
                                "seq": 0,
                                "storagePool": 1,
                                "storagePools": [
                                    1
                                ]
                            }
                        ],
                        "hardQuota": 1099511627776,
                        "id": 274,
                        "ida": "fec",
                        "largeObjectEnabled": True,
                        "lockedVaultEnabled": False,
                        "name": "testVaultName",
                        "nameIndexEnabled": True,
                        "privacyAlgorithm": "aont-rc4-128",
                        "privacyEnabled": True,
                        "readThreshold": None,
                        "recoveryListingEnabled": False,
                        "segmentSize": 4194304,
                        "softQuota": 879609302220,
                        "storageHealth": "ok",
                        "storagePoolGroup": 1,
                        "tags": [],
                        "threshold": 5,
                        "utilization": 0,
                        "uuid": "736a7f1e-e3da-4d4c-906d-97493e8e5bed",
                        "vaultFormat": "format5",
                        "vaultProxySettings": {},
                        "vaultPurpose": "standard",
                        "vaultType": "object",
                        "versioning": "disabled",
                        "width": 9,
                        "writeThreshold": 7
                    }
                ]
            },
            "responseHeader": {
                "now": 1491595126078,
                "requestId": "WOfvdQoQgF4AAHYXwZMAAAC3",
                "status": "ok"
            },
            "responseStatus": "ok"
        }
    },
    "itemType=account&id=95": {
        "status_code": "200",
        "text": {
            "responseData": {
                "accessPools": [],
                "accounts": [
                    {
                        "accessKeys": [
                            {
                                "accessKeyId": "XXXXXXXXXXXXXX",
                                "creationDate": "Thu, 30 Mar 2017 15:26:07 +0000",
                                "secretAccessKey": "YYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
                            }
                        ],
                        "creationDate": "Thu, 30 Mar 2017 15:24:17 +0000",
                        "email": None,
                        "enabled": True,
                        "id": 95,
                        "keystoneDomain": None,
                        "managerLocale": None,
                        "name": "KeyPairUser",
                        "organization": 1,
                        "privateAccountEnabled": False,
                        "roles": [
                            {
                                "role": "admin"
                            },
                            {
                                "role": "securityAdmin"
                            },
                            {
                                "role": "operator"
                            },
                            {
                                "role": "vaultProvisioner"
                            },
                            {
                                "role": "vaultUser",
                                "vaultPermissions": [
                                    {
                                        "permission": "owner",
                                        "vault": 274
                                    }
                                ]
                            }
                        ],
                        "timezone": None,
                        "type": "local",
                        "username": "testUsername",
                        "uuid": "AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEEE"
                    }
                ],
                "cabinets": [],
                "devices": [],
                "eventCategories": [],
                "fileServerPools": [],
                "fileSystems": [],
                "groups": [],
                "metadataClusters": [],
                "mirrors": [],
                "networkNodes": [],
                "shares": [],
                "sites": [],
                "storagePoolGroups": [],
                "storagePools": [],
                "tags": [],
                "vaults": []
            },
            "responseHeader": {
                "now": 1491594577080,
                "requestId": "WOftUAoQgF4AAHYXwR8AAACc",
                "status": "ok"
            },
            "responseStatus": "ok"
        }
    },
    "itemType=account&id=1": {
    	"status_code": "500",
	"text": "this is just a test"
    }
}
