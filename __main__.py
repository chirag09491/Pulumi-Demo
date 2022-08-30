"""A Python Pulumi program"""

import pulumi
import pulumi_oci as oci

###################Pulumi Test Configuration########
# test_user = oci.identity.User("test-user",
#                              compartment_id="ocid1.compartment.oc1..aaaaaaaax6uvmemkbtkybkq3omoh3ikrw7cmeywfmm2hinhgvhp2z4r7cvha",
#                              email="testuser@123.com",
#                              description="Test User Created by Pulumi")

# #configuration:

config=pulumi.Config()
compartment_ocid = config.require_secret('CompartmentOCID')

get_ad_name = oci.identity.get_availability_domain(
    compartment_id=compartment_ocid,
    ad_number=1
)

f = open("C:\\Users\\Chirag Sharma\\.ssh\\ssh-rsa.pub","r", encoding="utf8")
ssh_pub_key=f.read()
f.close()

node_image=oci.core.get_images(compartment_id=compartment_ocid,
                                             operating_system=config.get('Oracle Linux'),
                                             operating_system_version=config.get("8"),
                                             shape=config.get('VM.Standard.B1.8'),
                                             sort_by="TIMECREATED",
                                             sort_order="DESC")
                                             
                                             

#networking
# Note here we are passing OCI API functions and storing them in variables which holds reference for Pulumi,
# have no impact on infrastructure

vcn = oci.core.Vcn(
    "vcn_test_chirag",
    cidr_blocks = ['10.0.0.0/16'],
    display_name ="vcn_test_chirag",
    compartment_id = compartment_ocid
)


#pulumi.export("vcn_default_route_tbl_ocid",vcn.default_route_table_id)
#### Using existing VCN
# vcn = oci.core.get_vcn(vcn_id="ocid1.vcn.oc1.iad.amaaaaaa3vux2giacbjlhnyxsvrwvooywimy5qjeyfaqaq75hvwrkf3hk77a")
# node_subnet = oci.core.get_subnet(subnet_id="ocid1.subnet.oc1.iad.aaaaaaaakjsvu3ff5vabrkdz7qthwlc6sqthv5fc7w5xrjyz3bntxchiopta")
####

# nat_gateway = oci.core.NatGateway(
#     "nat-gateway_test_chirag",
#     compartment_id = compartment_ocid,
#     vcn_id=vcn.id
# )
internet_gateway = oci.core.InternetGateway(
    "oke_internet_gateway_TEST",
    compartment_id = compartment_ocid,
    vcn_id=vcn.id
)
test_route_table = oci.core.RouteTable(
    "ROUTE_TABLE_CHIRAG",
    compartment_id = compartment_ocid,
    vcn_id=vcn.id,
    display_name="ROUTE_TABLE_CHIRAG",
    route_rules=[oci.core.RouteTableRouteRuleArgs(
        network_entity_id=internet_gateway.id,
        destination="0.0.0.0/0",
        destination_type="CIDR_BLOCK"
        )]
)
test_security_list = oci.core.SecurityList(
    "Security_list_Chirag",
    compartment_id=compartment_ocid,
    vcn_id=vcn.id,
    display_name="Security_list_Chirag",
    egress_security_rules=[oci.core.SecurityListEgressSecurityRuleArgs(
        destination="0.0.0.0/0",
        destination_type="CIDR_BLOCK",
        icmp_options=oci.core.SecurityListIngressSecurityRuleIcmpOptionsArgs(
            type=3,
            code=4
        ),
        protocol="all"
    )],
    ingress_security_rules=[oci.core.SecurityListIngressSecurityRuleArgs(
        source_type="CIDR_BLOCK",
        source="0.0.0.0/0",       
        icmp_options=oci.core.SecurityListIngressSecurityRuleIcmpOptionsArgs(
            type=3,
            code=4
        ),
        protocol="all"
    )],
    #protocol="all"
)
node_subnet = oci.core.Subnet(
    "node_subnet_TEST",
    cidr_block = "10.0.10.0/24",
    compartment_id = compartment_ocid,
    vcn_id=vcn.id,
    security_list_ids=[test_security_list.id],
    route_table_id=test_route_table.id
)


instance_resource= oci.core.Instance(
    resource_name="Chirag_test_machine",
    display_name = "Chirag_test_machine",
    availability_domain="vzAG:US-ASHBURN-AD-1",
    compartment_id = compartment_ocid,
    create_vnic_details=oci.core.InstanceCreateVnicDetailsArgs(
        display_name="chirag_test_vnic",
        subnet_id=node_subnet.id
    ),
    fault_domain="FAULT-DOMAIN-1",
    metadata={"ssh_authorized_keys": ssh_pub_key},
    shape="VM.Standard.B1.8",
    shape_config=oci.core.InstanceShapeConfigArgs(
        memory_in_gbs=96,  ## Ram in GBs
        ocpus=8, ## number of CPU 
        ),
    # image="Oracle Linux 8",
    # vcn=vcn.id,
    source_details=oci.core.InstanceSourceDetailsArgs(
        boot_volume_size_in_gbs=55,
        source_id=node_image.images[0]['id'],
        source_type="image"
    ),
    state="RUNNING",
    )
pulumi.export("INstance_IP",instance_resource.public_ip)
    