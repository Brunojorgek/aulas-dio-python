from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(f"data oslo: {data_oslo}")
print(f"data são paulo: {data_sao_paulo}")