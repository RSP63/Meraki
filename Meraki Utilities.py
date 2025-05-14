#Meraki Utility

#pip install meraki

dashboard = meraki.DashboardAPI("your_api_key")

import meraki
import os, sys
import pprint
import constants
pp = pprint.PrettyPrinter


# Load the API key from an environment variable (recommended)
# or set it directly (not recommended for security reasons)


#To save as an environment variable, use following from terminal:
#export MERAKI_DASHBOARD_API_KEY=057ec3134334d3a2eb81fb35c9d3cdcca21b4b0f

#use 'printenv' to show environment variables

#API_KEY = os.environ.get("MERAKI_DASHBOARD_API_KEY")
#API_KEY = "057ec3134334d3a2eb81fb35c9d3cdcca21b4b0f"
API_KEY = constants.MERAKI_DASHBOARD_API_KEY


# Initialize the Dashboard API
dashboard = meraki.DashboardAPI(API_KEY)

# Get the list of organizations
my_orgs = dashboard.organizations.getOrganizations()
pprint.pp(my_orgs)

# Print the organization names
for org in my_orgs:
    print(org["name"])

#Networks:
try:
    networks = dashboard.organizations.getOrganizationNetworks(1077524)
except meraki.APIError as e:
    print(f'Meraki API error: {e}')
    print(f'status code = {e.status}')
    print(f'reason = {e.reason}')
    print(f'error = {e.message}')

print(networks)
for network in networks:
    print(f"Network: {network['name']}, Tags: {network['tags']}, Id,: {network['id']}, Product types: {network['productTypes']}, Time zone: {network['timeZone']}")


#Clients:
total_clients = 0
for net in networks:
    print(f'Finding clients in network {net["name"]}')
    try:
        # Get list of clients on network, filtering on timespan of last 14 days
        clients = dashboard.networks.getNetworkClients(net['id'], timespan=60 * 60 * 24 * 14, perPage=1000, total_pages='all')
    except meraki.APIError as e:
        print(f'Meraki API error: {e}')
        print(f'status code = {e.status}')
        print(f'reason = {e.reason}')
        print(f'error = {e.message}')
    except Exception as e:
        print(f'some other error: {e}')
    else:
        if clients:
            # Write to file
            # file_name = f'{net["name"]}.csv'
            #output_file = open(f'{folder_name}/{file_name}', mode='w', newline='\n')
            # field_names = clients[0].keys()
            # csv_writer = csv.DictWriter(output_file, field_names, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            # csv_writer.writeheader()
            # csv_writer.writerows(clients)
            #output_file.close()
            #pprint.pp(clients)
            print(f'Found {len(clients)} clients in this network')
            total_client += len(clients)
print(f'Found {len(clients)} total clients in all network')
