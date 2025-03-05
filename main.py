import requests

url = "https://www.yanolja.com/api/v1/leisure/v3/cross_sell/region/widget?placeType=hotel&region=910107"

payload = {}
headers = {
    'cookie': 'trackcode=mkt_google_sa; app-device=etc; yanolja_sid=s%3AgO-qejpRh_eSsZ-lkP8QHKpmhvkHt3rA.eJtIQK3fukdJpcBK0rAMxsLpcQZpXXTVLZyFfNtTomk; __cf_bm=gBWjQwD9sW13JbQdNlEFyK0AhGOHGSsq7igrmJn_p88-1739788078-1.0.1.1-VBMX5sl_Y0cL2mZnwPtuMb2cvpvIQba2BZ5I5Ud40S6vuVXO1Za9DRtalqMb8mQXM70toq8oqyzkvpL_k.bObw; _cfuvid=WrnuQ9paghQHsLgS3tjLJuC5Xn3Ilnr5Wy8xWJBfl9Y-1739788078062-0.0.1.1-604800000; cf_clearance=kNNgSa402CKYlwbj._oE83DBtQoxPPuIWKyibM2bRF0-1739788079-1.2.1.1-EOJ_RDX9QfyFBAdKjSh8.vKosgdXHyuW4mQ1.Jo_u3iuOo.F2k3mongeKu2baqQVdSYzL1aXi4QgGtMBfNH7_7mAivRZJEJGree2C7LoVeJ05BBwnEygG3iDR7WqLsMe6ItA4iKy9OPddjpgr5GIAOrpWe91Iw9IWtVI6qeut9FCYj8r7xma9QA.nxl7MZuwISO6j0kP5LZo7x72VKCjOcSLzNeGCP7CwnH2MK8yM.Y0g7lY7ios4P.oDkmS1PvGQrmSO6AoxJOS6EPZzvqsxcY97ShmVpCXdYeuDQUirh4; _fbp=fb.1.1739788080699.959762704442668752; ACEFCID=UID-67B30F458B121C2C40031CDE; ACEUACS=undefined; _fwb=143D0De2mipQDvsccKwdst8.1739788101715; AUAH5A41667571241=1739788101647385881%7C2%7C1739788101647385881%7C1%7C1739788101703J02WY3%7C1; ASAH5A41667571241=1739788101647385881%7C1739788426665733715%7C1739788101647385881%7C0%7Chttpswwwyanoljacomsub-homehotel; ARAH5A41667571241=httpswwwyanoljacomapiv1local-accommodationv2search20Request20Method20POSTbookmark; capacity-domestic=[2,0,[]]; cto_bundle=daYS4V9vSTJKWEhMc3RQQlpWSVJSdnJPajZ4ZU1Ra1l5QkJaT0hValE4TyUyQlp1a2lwZG14OHkwelRSNjNFTlFVQVl6ayUyRkVZbzZqdU5PV2ZpJTJGeklwaVozTCUyQmZpNDdSYWxsY1dtbkxHeHE2OU81U0xpZTFQZHZWWm9rZktFQ1FYVmNZQVJXJTJCWEVWczM1ZDZMJTJGdmhBYlBUelR4bkR4TDZ3WVd5VkV3eVZLekF0WmpWJTJCMyUyQnlLOGhBWTNzOUtsYnNYNlYlMkZyT0NDJTJCOWhLYlA2V1RWUmlzbUg5R2RTRGclM0QlM0Q; _gid=GA1.2.14380716.1739788470; cgntId=ap-northeast-2%3A9fdb715b-630c-c6b3-6c55-38e2a754f7d8; wcs_bt=ae93a192ec48a4:1739788549; _ga=GA1.1.1928649838.1739788102; _ga_8KQT8SBL6R=GS1.1.1739788101.1.1.1739788549.60.0.0; location={%22latitude%22:%2237.50681%22%2C%22longitude%22:%22127.06624%22%2C%22locationType%22:%22DEFAULT%22%2C%22locationTime%22:1739788100%2C%22hasPermissionError%22:false}; _ga_JVPP9KTQGG=GS1.1.1739788102.1.1.1739788550.59.0.0; __cf_bm=cRyI1MaAGppCqepvyRE7poAan1DbC5d5mW68smRibVU-1739789158-1.0.1.1-VZ_pd1GfhNyahBaNmRbhMe.9hj0F9Qp7m04YWiV.X1sJz1W7XHHgCDa5vovpSitv3MF4BHXFk9Q9UmNFGBan5w; _cfuvid=AEg.Wl63X6VAPhxoDXQ2Q_8r2Jh2Y4hCDzD0Xs8tTTw-1739788969055-0.0.1.1-604800000; app-device=etc; cgntId=ap-northeast-2%3A9fdb715b-630c-c6b3-6c55-38e2a754f7d8; yanolja_sid=s%3AgO-qejpRh_eSsZ-lkP8QHKpmhvkHt3rA.eJtIQK3fukdJpcBK0rAMxsLpcQZpXXTVLZyFfNtTomk',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': '',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
