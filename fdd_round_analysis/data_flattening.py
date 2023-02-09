# Required modules
import sys
import pandas as pd
from pandas.io.json import json_normalize
import json
import numpy as np

# Gitcoin protocol datasets
file_path_applications = 'data/oss_round_applications.json'
file_path_votes = 'data/oss_round_votes_raw.json'
round_name = 'oss'


def vote_processing(df_votes):
    # Votes data
    votes_dataset  = df_votes

    votes_dataset.rename(columns = {
    'from': 'source_wallet',
    'to': 'project_wallet',
    'createdAt': 'created_at'}, inplace = True)

    votes_dataset['source_wallet'] = votes_dataset['source_wallet'].str.lower()
    votes_dataset['project_wallet'] = votes_dataset['project_wallet'].str.lower()

    votes_dataset['created_at'] = pd.to_datetime( votes_dataset['created_at'],unit='s')

    currencies = {
            "0x6b175474e89094c44da98b954eedeac495271d0f": {
                "symbol": "DAI",
                "decimals": 18,
            },
            "0x0000000000000000000000000000000000000000": {
                "symbol": "ETH",
                "decimals": 18,
            },
        }

    votes_dataset["amount"] = votes_dataset.apply(lambda x: int(x.amount) / 10 ** currencies[x.token]["decimals"], axis=1)
    votes_dataset["token"] = votes_dataset.token.apply(lambda x: currencies[x]["symbol"])

    return votes_dataset


def application_processing(df_projects, round_name):
    # Project grant applications
    projects_dataset = pd.DataFrame()

    for i in df_projects['projects'][0]:
        temp_df = pd.json_normalize(i)
        responses = pd.json_normalize(temp_df['ipfs.application.answers'])
        temp_df = temp_df.join([responses])

        projects_dataset  = pd.concat([projects_dataset, temp_df], ignore_index=True)

    if round_name == 'climate':
        projects_dataset = projects_dataset[[
            'ipfs.application.round',	
            'ipfs.application.recipient',	
            'ipfs.application.project.lastUpdated',	
            'ipfs.application.project.id',	
            'ipfs.application.project.title',	
            'ipfs.application.project.description',	
            'ipfs.application.project.website',
            'ipfs.application.project.userGithub',	
            'ipfs.application.project.projectGithub',
            'ipfs.application.project.projectTwitter',
            1,
            2,
            'createdAt',
            'updatedAt'
        ]]

        projects_dataset.rename(columns = {
        'ipfs.application.round': 'application_round',	
        'ipfs.application.recipient': 'project_wallet',	
        'ipfs.application.project.lastUpdated': 'last_updated',	
        'ipfs.application.project.id': 'project_id',	
        'ipfs.application.project.title': 'title',	
        'ipfs.application.project.description': 'description',	
        'ipfs.application.project.website': 'website',
        'ipfs.application.project.userGithub': 'github_user',	
        'ipfs.application.project.projectGithub': 'project_github',
        'ipfs.application.project.projectTwitter':'project_twitter',
        1: 'previous_funding',
        2: 'team_size',
        'createdAt': 'created_at', 
        'updatedAt': 'updated_at'
        }, inplace = True)
    
        # Unnest answers for each grant application
        question_col = ['previous_funding','team_size']

        for col in question_col:
            col_update = []

            for item in projects_dataset[col]:
                if 'answer' in item:
                    col_update.append(item['answer'])
                else:
                    col_update.append(np.nan)

            projects_dataset[col] = col_update


    elif round_name == 'oss':
        projects_dataset = projects_dataset[[
            'ipfs.application.round',	
            'ipfs.application.recipient',	
            'ipfs.application.project.lastUpdated',	
            'ipfs.application.project.id',	
            'ipfs.application.project.title',	
            'ipfs.application.project.description',	
            'ipfs.application.project.website',
            'ipfs.application.project.userGithub',	
            'ipfs.application.project.projectGithub',
            'ipfs.application.project.projectTwitter',
            1,
            2,
            3,
            4,
            'createdAt',
            'updatedAt'
        ]]

        projects_dataset.rename(columns = {
        'ipfs.application.round': 'application_round',	
        'ipfs.application.recipient': 'project_wallet',	
        'ipfs.application.project.lastUpdated': 'last_updated',	
        'ipfs.application.project.id': 'project_id',	
        'ipfs.application.project.title': 'title',	
        'ipfs.application.project.description': 'description',	
        'ipfs.application.project.website': 'website',
        'ipfs.application.project.userGithub': 'github_user',	
        'ipfs.application.project.projectGithub': 'project_github',
        'ipfs.application.project.projectTwitter':'project_twitter',
        1: 'previous_funding',
        2: 'team_size',
        3: 'verified_twitter_or_github',
        4: 'links_to_github_or_org',
        'createdAt': 'created_at', 
        'updatedAt': 'updated_at'
        }, inplace = True)
    
        # Unnest answers for each grant application
        question_col = ['previous_funding','team_size', 'verified_twitter_or_github', 'links_to_github_or_org']

        for col in question_col:
            col_update = []

            for item in projects_dataset[col]:
                if 'answer' in item:
                    col_update.append(item['answer'])
                else:
                    col_update.append(np.nan)

            projects_dataset[col] = col_update

    elif round_name == 'ethereum':
        projects_dataset = projects_dataset[[
            'ipfs.application.round',	
            'ipfs.application.recipient',	
            'ipfs.application.project.lastUpdated',	
            'ipfs.application.project.id',	
            'ipfs.application.project.title',	
            'ipfs.application.project.description',	
            'ipfs.application.project.website',
            'ipfs.application.project.userGithub',	
            'ipfs.application.project.projectGithub',
            'ipfs.application.project.projectTwitter',
            1,
            2,
            3,
            'createdAt',
            'updatedAt'
        ]]

        projects_dataset.rename(columns = {
        'ipfs.application.round': 'application_round',	
        'ipfs.application.recipient': 'project_wallet',	
        'ipfs.application.project.lastUpdated': 'last_updated',	
        'ipfs.application.project.id': 'project_id',	
        'ipfs.application.project.title': 'title',	
        'ipfs.application.project.description': 'description',	
        'ipfs.application.project.website': 'website',
        'ipfs.application.project.userGithub': 'github_user',	
        'ipfs.application.project.projectGithub': 'project_github',
        'ipfs.application.project.projectTwitter':'project_twitter',
        1: 'previous_funding',
        2: 'team_size',
        3: 'verified_twitter_or_github',
        'createdAt': 'created_at', 
        'updatedAt': 'updated_at'
        }, inplace = True)
    
        # Unnest answers for each grant application
        question_col = ['previous_funding','team_size', 'verified_twitter_or_github']

        for col in question_col:
            col_update = []

            for item in projects_dataset[col]:
                if 'answer' in item:
                    col_update.append(item['answer'])
                else:
                    col_update.append(np.nan)

            projects_dataset[col] = col_update

    else:
        projects_dataset = projects_dataset[[
            'ipfs.application.round',	
            'ipfs.application.recipient',	
            'ipfs.application.project.lastUpdated',	
            'ipfs.application.project.id',	
            'ipfs.application.project.title',	
            'ipfs.application.project.description',	
            'ipfs.application.project.website',
            'ipfs.application.project.userGithub',	
            'ipfs.application.project.projectGithub',
            'ipfs.application.project.projectTwitter',
            1,
            2,
            'createdAt',
            'updatedAt'
        ]]

        projects_dataset.rename(columns = {
        'ipfs.application.round': 'application_round',	
        'ipfs.application.recipient': 'project_wallet',	
        'ipfs.application.project.lastUpdated': 'last_updated',	
        'ipfs.application.project.id': 'project_id',	
        'ipfs.application.project.title': 'title',	
        'ipfs.application.project.description': 'description',	
        'ipfs.application.project.website': 'website',
        'ipfs.application.project.userGithub': 'github_user',	
        'ipfs.application.project.projectGithub': 'project_github',
        'ipfs.application.project.projectTwitter':'project_twitter',
        1: 'previous_funding',
        2: 'team_size',
        'createdAt': 'created_at', 
        'updatedAt': 'updated_at'
        }, inplace = True)
    
        # Unnest answers for each grant application
        question_col = ['previous_funding','team_size']

        for col in question_col:
            col_update = []

            for item in projects_dataset[col]:
                if 'answer' in item:
                    col_update.append(item['answer'])
                else:
                    col_update.append(np.nan)

            projects_dataset[col] = col_update

    # Update Unix to ISO dates
    projects_dataset['created_at'] = pd.to_datetime( projects_dataset['created_at'],unit='s')
    projects_dataset['updated_at'] = pd.to_datetime( projects_dataset['updated_at'],unit='s')

    projects_dataset['project_wallet'] = projects_dataset['project_wallet'].str.lower()

    return projects_dataset


def processing(file_app, file_votes, round_name):

    with open(file_app) as fp:
        s_app = json.load(fp)

    with open(file_votes) as fp:
        s_votes = json.load(fp)

    # flattened df, where nested keys -> column as `key1.key2.key_last`
    df_projects = pd.json_normalize(s_app)
    df_votes = pd.json_normalize(s_votes)

    vote_df = vote_processing(df_votes)
    app_df = application_processing(df_projects, round_name)

    data_join = pd.merge(vote_df, app_df, how="left", on=['project_wallet'])


    return vote_df, app_df, data_join

if __name__ == '__main__':  
    processing(file_path_applications, file_path_votes, round_name)