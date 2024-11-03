import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

urls = [
    "https://fbref.com/en/squads/b8fd03ef/2023-2024/Manchester-City-Stats",
    "https://fbref.com/en/squads/1df6b87e/2023-2024/Sheffield-United-Stats"
    "https://fbref.com/en/squads/e4a775cb/2023-2024/Nottingham-Forest-Stats",
    "https://fbref.com/en/squads/e297cd13/2023-2024/Luton-Town-Stats",
    "https://fbref.com/en/squads/943e8050/2023-2024/Burnley-Stats",
    "https://fbref.com/en/squads/18bb7c10/2023-2024/Arsenal-Stats",
    "https://fbref.com/en/squads/822bd0ba/2023-2024/Liverpool-Stats",
    "https://fbref.com/en/squads/8602292d/2023-2024/Aston-Villa-Stats",
    "https://fbref.com/en/squads/361ca564/2023-2024/Tottenham-Hotspur-Stats",
    "https://fbref.com/en/squads/cff3d9bb/2023-2024/Chelsea-Stats",
    "https://fbref.com/en/squads/b2b47a98/2023-2024/Newcastle-United-Stats",
    "https://fbref.com/en/squads/19538871/2023-2024/Manchester-United-Stats",
    "https://fbref.com/en/squads/7c21e445/2023-2024/West-Ham-United-Stats",
    "https://fbref.com/en/squads/47c64c55/2023-2024/Crystal-Palace-Stats",
    "https://fbref.com/en/squads/d07537b9/2023-2024/Brighton-and-Hove-Albion-Stats",
    "https://fbref.com/en/squads/4ba7cbea/2023-2024/Bournemouth-Stats",
    "https://fbref.com/en/squads/fd962109/2023-2024/Fulham-Stats",
    "https://fbref.com/en/squads/8cec06e1/2023-2024/Wolverhampton-Wanderers-Stats",
    "https://fbref.com/en/squads/d3fd31cc/2023-2024/Everton-Stats",
    "https://fbref.com/en/squads/cd051869/2023-2024/Brentford-Stats",
]
combined_data = []

def extract_team_name(url):
    match = re.search(r'/([A-Za-z0-9-]+)-Stats$', url)
    if match:
        return match.group(1).replace('-', ' ')
    return None

def collect_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    team_name = extract_team_name(url)

    standard_table = soup.find('table', attrs={'class':'stats_table sortable min_width','id':'stats_standard_9'})
    if standard_table:
        rows = standard_table.find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                standard_data = {
                    'Player': row.find('th').text.strip(),
                    'Nation': cols[0].text.strip(),
                    'Team': team_name,
                    'Position': cols[1].text.strip(),
                    'Age': cols[2].text.strip(),
                    'Playing time: Matches Played': cols[3].text.strip(),
                    'Playing time: Starts': cols[4].text.strip(),
                    'Playing time: Minutes': int(cols[5].text.strip().replace(',','')) if(cols[5].text.strip().replace(',','').isdigit()) else 0,
                    'Performances: Non-Penalty Goals': cols[10].text.strip(),
                    'Performances: Penalty Goals': cols[11].text.strip(),
                    'Performances: Assists': cols[8].text.strip(),
                    'Performances: Yellow Cards': cols[13].text.strip(),
                    'Performances: Red Cards': cols[14].text.strip(),
                    'Expected: xG': cols[15].text.strip(),
                    'Expected: npxG': cols[16].text.strip(),
                    'Expected: xAG': cols[17].text.strip(),
                    'Progression: PrgC': cols[19].text.strip(),
                    'Progression: PrgP': cols[20].text.strip(),
                    'Progression: PrgR': cols[21].text.strip(),
                    'Per 90 minutes: Gls': cols[22].text.strip(),
                    'Per 90 minutes: Ast': cols[23].text.strip(),
                    'Per 90 minutes: G+A': cols[24].text.strip(),
                    'Per 90 minutes: G-PK': cols[25].text.strip(),
                    'Per 90 minutes: G+A-PK': cols[26].text.strip(),
                    'Per 90 minutes: xG + xAG': cols[29].text.strip(),
                    'Per 90 minutes: npxG + xAG': cols[31].text.strip(),
                    'Performances: GA': 'N/a',
                    'Performances: GA90': 'N/a',
                    'Performances: SoTA': 'N/a',
                    'Performances: Saves': 'N/a',
                    'Performances: Save%': 'N/a',
                    'Performances: W': 'N/a',
                    'Performances: D': 'N/a',
                    'Performances: L': 'N/a',
                    'Performances: CS': 'N/a',
                    'Performances: CS%': 'N/a',
                    'Penalty Kicks: PKatt': 'N/a',
                    'Penalty Kicks: PKA': 'N/a',
                    'Penalty Kicks: PKsv': 'N/a',
                    'Penalty Kicks: PKm': 'N/a',
                    'Penalty Kicks: PK Save%': 'N/a',
                    'Standard: Gls': 'N/a',
                    'Standard: Sh': 'N/a',
                    'Standard: SoT': 'N/a',
                    'Standard: SoT%': 'N/a',
                    'Standard: Sh/90': 'N/a',
                    'Standard: Sot/90': 'N/a',
                    'Standard: G/Sh': 'N/a',
                    'Standard: G/SoT': 'N/a',
                    'Standard: Dist': 'N/a',
                    'Standard: FK': 'N/a',
                    'Standard: PK': 'N/a',
                    'Standard: PKatt': 'N/a',
                    'Expected: npxG/Sh': 'N/a',
                    'Expected: G-xG': 'N/a',
                    'Expected: np:G-xG': 'N/a',
                    'Total: Cmp': 'N/a',
                    'Total: Att': 'N/a',
                    'Total: Cmp%': 'N/a',
                    'Total: TotDist': 'N/a',
                    'Total: PrgDist': 'N/a',
                    'Short: Cmp': 'N/a',
                    'Short: Att': 'N/a',
                    'Short: Cmp%': 'N/a',
                    'Medium: Cmp': 'N/a',
                    'Medium: Att': 'N/a',
                    'Medium: Cmp%': 'N/a',
                    'Long: Cmp': 'N/a',
                    'Long: Att': 'N/a',
                    'Long: Cmp%': 'N/a',
                    'Expected: Ast': 'N/a',
                    'Expected: xA': 'N/a',
                    'Expected: A-xAG': 'N/a',
                    'Expected: KP': 'N/a',
                    'Expected: 1/3': 'N/a',
                    'Expected: PPA': 'N/a',
                    'Expected: CrsPA': 'N/a',
                    'Expected: PrgP': 'N/a',
                    'Pass Types: Live': 'N/a',
                    'Pass Types: Dead': 'N/a',
                    'Pass Types: FK': 'N/a',
                    'Pass Types: TB': 'N/a',
                    'Pass Types: Sw': 'N/a',
                    'Pass Types: Crs': 'N/a',
                    'Pass Types: TI': 'N/a',
                    'Pass Types: CK': 'N/a',
                    'Corner Kicks: In': 'N/a',
                    'Corner Kicks: Out': 'N/a',
                    'Corner Kicks: Str': 'N/a',
                    'Outcomes: Cmp': 'N/a',
                    'Outcomes: Off': 'N/a',
                    'Outcomes: Blocks': 'N/a',
                    'SCA: SCA': 'N/a',
                    'SCA: SCA90': 'N/a',
                    'SCA Types: PassLive': 'N/a',
                    'SCA Types: PassDead': 'N/a',
                    'SCA Types: TO': 'N/a',
                    'SCA Types: Sh': 'N/a',
                    'SCA Types: Fld': 'N/a',
                    'SCA Types: Def': 'N/a',
                    'GCA: GCA': 'N/a',
                    'GCA: GCA90': 'N/a',
                    'GCA Types: PassLive': 'N/a',
                    'GCA Types: PassDead': 'N/a',
                    'GCA Types: TO': 'N/a',
                    'GCA Types: Sh': 'N/a',
                    'GCA Types: Fld': 'N/a',
                    'GCA Types: Def': 'N/a',
                    'Tackles: Tkl': 'N/a',
                    'Tackles: TklW': 'N/a',
                    'Tackles: Def 3rd': 'N/a',
                    'Tackles: Mid 3rd': 'N/a',
                    'Tackles: Att 3rd': 'N/a',
                    'Challenges: Tkl': 'N/a',
                    'Challenges: Att': 'N/a',
                    'Challenges: Tkl%': 'N/a',
                    'Challenges: Lost': 'N/a',
                    'Blocks: Blocks': 'N/a',
                    'Blocks: Sh': 'N/a',
                    'Blocks: Pass': 'N/a',
                    'Blocks: Int': 'N/a',
                    'Blocks: Tkl + Int': 'N/a',
                    'Blocks: Clr': 'N/a',
                    'Blocks: Err': 'N/a',
                    'Touches: Touches': 'N/a',
                    'Touches: Def Pen': 'N/a',
                    'Touches: Def 3rd': 'N/a',
                    'Touches: Mid 3rd': 'N/a',
                    'Touches: Att 3rd': 'N/a',
                    'Touches: Att Pen': 'N/a',
                    'Touches: Live': 'N/a',
                    'Take-Ons: Att': 'N/a',
                    'Take-Ons: Succ': 'N/a',
                    'Take-Ons: Succ%': 'N/a',
                    'Take-Ons: Tkld': 'N/a',
                    'Take-Ons: Tkld%': 'N/a',
                    'Carries: Carries': 'N/a',
                    'Carries: TotDist': 'N/a',
                    'Carries: ProDist': 'N/a',
                    'Carries: ProgC': 'N/a',
                    'Carries: 1/3': 'N/a',
                    'Carries: CPA': 'N/a',
                    'Carries: Mis': 'N/a',
                    'Carries: Dis': 'N/a',
                    'Receiving: Rec': 'N/a',
                    'Receiving: PrgR': 'N/a',
                    'Starts: Starts': 'N/a',
                    'Starts: Mn/Start': 'N/a',
                    'Starts: Compl': 'N/a',
                    'Subs: Subs': 'N/a',
                    'Subs: Mn/Sub': 'N/a',
                    'Subs: unSub': 'N/a',
                    'Team Success: PPM': 'N/a',
                    'Team Success: onG': 'N/a',
                    'Team Success: onGA': 'N/a',
                    'Team Success xG: onxG': 'N/a',
                    'Team Success xG: onxGA': 'N/a',
                    'Performance: Fls': 'N/a',
                    'Performance: Fld': 'N/a',
                    'Performance: Off': 'N/a',
                    'Performance: Crs': 'N/a',
                    'Performance: OG': 'N/a',
                    'Performance: Recov': 'N/a',
                    'Aerial Duels: Won': 'N/a',
                    'Aerial Duels: Lost': 'N/a',
                    'Aerial Duels: Won%': 'N/a',
                }
                if standard_data['Playing time: Minutes'] > 90:
                    combined_data.append(standard_data)

    goalkeeping_table = soup.find('table', attrs={'class':'stats_table sortable min_width','id':'stats_keeper_9'})
    if goalkeeping_table:
        rows = goalkeeping_table.find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                for player in combined_data:
                    if player['Player']==row.find('th').text.strip() and player['Age']==cols[2].text.strip():
                        player['Performances: GA']=cols[7].text.strip()
                        player['Performances: GA90']=cols[8].text.strip()
                        player['Performances: SoTA']=cols[9].text.strip()
                        player['Performances: Saves']=cols[10].text.strip()
                        player['Performances: Save%']=cols[11].text.strip()
                        player['Performances: W']=cols[12].text.strip()
                        player['Performances: D']=cols[13].text.strip()
                        player['Performances: L']=cols[14].text.strip()
                        player['Performances: CS']=cols[15].text.strip()
                        player['Performances: CS%']=cols[16].text.strip()
                        player['Penalty Kicks: PKatt']=cols[17].text.strip()
                        player['Penalty Kicks: PKA']=cols[18].text.strip()
                        player['Penalty Kicks: PKsv']=cols[19].text.strip()
                        player['Penalty Kicks: PKm']=cols[20].text.strip()
                        player['Penalty Kicks: PK Save%']=cols[21].text.strip()

    shooting_table=soup.find('table', attrs={'class':'stats_table sortable min_width','id':'stats_shooting_9'})
    if shooting_table:
        rows = shooting_table.find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                for player in combined_data:
                    if player['Player']==row.find('th').text.strip() and player['Age']==cols[2].text.strip():
                        player['Standard: Gls']=cols[4].text.strip()
                        player['Standard: Sh']=cols[5].text.strip()
                        player['Standard: SoT']=cols[6].text.strip()
                        player['Standard: SoT%']=cols[7].text.strip()
                        player['Standard: Sh/90']=cols[8].text.strip()
                        player['Standard: Sot/90']=cols[9].text.strip()
                        player['Standard: G/Sh']=cols[10].text.strip()
                        player['Standard: G/SoT']=cols[11].text.strip()
                        player['Standard: Dist']=cols[12].text.strip()
                        player['Standard: FK']=cols[13].text.strip()
                        player['Standard: PK']=cols[14].text.strip()
                        player['Standard: PKatt']=cols[15].text.strip()
                        player['Expected: npxG/Sh']=cols[18].text.strip()
                        player['Expected: G-xG']=cols[19].text.strip()
                        player['Expected: np:G-xG']=cols[20].text.strip()

    passing_table=soup.find('table', attrs={'class':'stats_table sortable min_width','id':'stats_passing_9'})
    if passing_table:
        rows = passing_table.find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                for player in combined_data:
                    if player['Player']==row.find('th').text.strip() and player['Age']==cols[2].text.strip():
                        player['Total: Cmp']=cols[4].text.strip()
                        player['Total: Att']=cols[5].text.strip()
                        player['Total: Cmp%']=cols[6].text.strip()
                        player['Total: TotDist']=cols[7].text.strip()
                        player['Total: PrgDist']=cols[8].text.strip()
                        player['Short: Cmp']=cols[9].text.strip()
                        player['Short: Att']=cols[10].text.strip()
                        player['Short: Cmp%']=cols[11].text.strip()
                        player['Medium: Cmp']=cols[12].text.strip()
                        player['Medium: Att']=cols[13].text.strip()
                        player['Medium: Cmp%']=cols[14].text.strip()
                        player['Long: Cmp']=cols[15].text.strip()
                        player['Long: Att']=cols[16].text.strip()
                        player['Long: Cmp%']=cols[17].text.strip()
                        player['Expected: Ast']=cols[18].text.strip()
                        player['Expected: xA']=cols[20].text.strip()
                        player['Expected: A-xAG']=cols[21].text.strip()
                        player['Expected: KP']=cols[22].text.strip()
                        player['Expected: 1/3']=cols[23].text.strip()
                        player['Expected: PPA']=cols[24].text.strip()
                        player['Expected: CrsPA']=cols[25].text.strip()
                        player['Expected: PrgP']=cols[26].text.strip()

    passtype_table=soup.find('table', attrs={'class':'stats_table sortable min_width','id':'stats_passing_types_9'})
    if passtype_table:
        rows = passtype_table.find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                for player in combined_data:
                    if player['Player']==row.find('th').text.strip() and player['Age']==cols[2].text.strip():
                        player['Pass Types: Live']=cols[5].text.strip()
                        player['Pass Types: Dead']=cols[6].text.strip()
                        player['Pass Types: FK']=cols[7].text.strip()
                        player['Pass Types: TB']=cols[8].text.strip()
                        player['Pass Types: Sw']=cols[9].text.strip()
                        player['Pass Types: Crs']=cols[10].text.strip()
                        player['Pass Types: TI']=cols[11].text.strip()
                        player['Pass Types: CK']=cols[12].text.strip()
                        player['Corner Kicks: In']=cols[13].text.strip()
                        player['Corner Kicks: Out']=cols[14].text.strip()
                        player['Corner Kicks: Str']=cols[15].text.strip()
                        player['Outcomes: Cmp']=cols[16].text.strip()
                        player['Outcomes: Off']=cols[17].text.strip()
                        player['Outcomes: Blocks']=cols[18].text.strip()

    goalshot_table=soup.find('table', attrs={'class':'stats_table sortable min_width','id':'stats_gca_9'})
    if goalshot_table:
        rows = goalshot_table.find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                for player in combined_data:
                    if player['Player']==row.find('th').text.strip() and player['Age']==cols[2].text.strip():
                        player['SCA: SCA']=cols[4].text.strip()
                        player['SCA: SCA90']=cols[5].text.strip()
                        player['SCA Types: PassLive']=cols[6].text.strip()
                        player['SCA Types: PassDead']=cols[7].text.strip()
                        player['SCA Types: TO']=cols[8].text.strip()
                        player['SCA Types: Sh']=cols[9].text.strip()
                        player['SCA Types: Fld']=cols[10].text.strip()
                        player['SCA Types: Def']=cols[11].text.strip()
                        player['GCA: GCA']=cols[12].text.strip()
                        player['GCA: GCA90']=cols[13].text.strip()
                        player['GCA Types: PassLive']=cols[14].text.strip()
                        player['GCA Types: PassDead']=cols[15].text.strip()
                        player['GCA Types: TO']=cols[16].text.strip()
                        player['GCA Types: Sh']=cols[17].text.strip()
                        player['GCA Types: Fld']=cols[18].text.strip()
                        player['GCA Types: Def']=cols[19].text.strip()

    defense_table=soup.find('table', attrs={'class':'stats_table sortable min_width','id':'stats_defense_9'})
    if defense_table:
        rows = defense_table.find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                for player in combined_data:
                    if player['Player']==row.find('th').text.strip() and player['Age']==cols[2].text.strip():
                        player['Tackles: Tkl']=cols[4].text.strip()
                        player['Tackles: TklW']=cols[5].text.strip()
                        player['Tackles: Def 3rd']=cols[6].text.strip()
                        player['Tackles: Mid 3rd']=cols[7].text.strip()
                        player['Tackles: Att 3rd']=cols[8].text.strip()
                        player['Challenges: Tkl']=cols[9].text.strip()
                        player['Challenges: Att']=cols[10].text.strip()
                        player['Challenges: Tkl%']=cols[11].text.strip()
                        player['Challenges: Lost']=cols[12].text.strip()
                        player['Blocks: Blocks']=cols[13].text.strip()
                        player['Blocks: Sh']=cols[14].text.strip()
                        player['Blocks: Pass']=cols[15].text.strip()
                        player['Blocks: Int']=cols[16].text.strip()
                        player['Blocks: Tkl + Int']=cols[17].text.strip()
                        player['Blocks: Clr']=cols[18].text.strip()
                        player['Blocks: Err']=cols[19].text.strip()

    possession_table=soup.find('table', attrs={'class':'stats_table sortable min_width','id':'stats_possession_9'})
    if possession_table:
        rows = possession_table.find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                for player in combined_data:
                    if player['Player']==row.find('th').text.strip() and player['Age']==cols[2].text.strip():
                        player['Touches: Touches']=cols[4].text.strip()
                        player['Touches: Def Pen']=cols[5].text.strip()
                        player['Touches: Def 3rd']=cols[6].text.strip()
                        player['Touches: Mid 3rd']=cols[7].text.strip()
                        player['Touches: Att 3rd']=cols[8].text.strip()
                        player['Touches: Att Pen']=cols[9].text.strip()
                        player['Touches: Live']=cols[10].text.strip()
                        player['Take-Ons: Att']=cols[11].text.strip()
                        player['Take-Ons: Succ']=cols[12].text.strip()
                        player['Take-Ons: Succ%']=cols[13].text.strip()
                        player['Take-Ons: Tkld']=cols[14].text.strip()
                        player['Take-Ons: Tkld%']=cols[15].text.strip()
                        player['Carries: Carries']=cols[16].text.strip()
                        player['Carries: TotDist']=cols[17].text.strip()
                        player['Carries: ProDist']=cols[18].text.strip()
                        player['Carries: ProgC']=cols[19].text.strip()
                        player['Carries: 1/3']=cols[20].text.strip()
                        player['Carries: CPA']=cols[21].text.strip()
                        player['Carries: Mis']=cols[22].text.strip()
                        player['Carries: Dis']=cols[23].text.strip()
                        player['Receiving: Rec']=cols[24].text.strip()
                        player['Receiving: PrgR']=cols[25].text.strip()

    playtime_table=soup.find('table', attrs={'class':'stats_table sortable min_width','id':'stats_playing_time_9'})
    if playtime_table:
        rows = playtime_table.find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                for player in combined_data:
                    if player['Player']==row.find('th').text.strip() and player['Age']==cols[2].text.strip():
                        player['Starts: Starts']=cols[8].text.strip()
                        player['Starts: Mn/Start']=cols[9].text.strip()
                        player['Starts: Compl']=cols[10].text.strip()
                        player['Subs: Subs']=cols[11].text.strip()
                        player['Subs: Mn/Sub']=cols[12].text.strip()
                        player['Subs: unSub']=cols[13].text.strip()
                        player['Team Success: PPM']=cols[14].text.strip()
                        player['Team Success: onG']=cols[15].text.strip()
                        player['Team Success: onGA']=cols[16].text.strip()
                        player['Team Success xG: onxG']=cols[20].text.strip()
                        player['Team Success xG: onxGA']=cols[21].text.strip()

    miscellaneous_table=soup.find('table', attrs={'class':'stats_table sortable min_width','id':'stats_misc_9'})
    if miscellaneous_table:
        rows = miscellaneous_table.find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if cols:
                for player in combined_data:
                    if player['Player']==row.find('th').text.strip() and player['Age']==cols[2].text.strip():
                        player['Performance: Fls']=cols[7].text.strip()
                        player['Performance: Fld']=cols[8].text.strip()
                        player['Performance: Off']=cols[9].text.strip()
                        player['Performance: Crs']=cols[10].text.strip()
                        player['Performance: OG']=cols[15].text.strip()
                        player['Performance: Recov']=cols[16].text.strip()
                        player['Aerial Duels: Won']=cols[17].text.strip()
                        player['Aerial Duels: Lost']=cols[18].text.strip()
                        player['Aerial Duels: Won%']=cols[19].text.strip()

for url in urls:
    collect_data(url)
combined_df = pd.DataFrame(combined_data)
combined_df.sort_values(by=['Player', 'Age'], ascending=[True, False], inplace=True)
combined_df.fillna('N/a', inplace=True)
combined_df.to_csv('results.csv', index=False)