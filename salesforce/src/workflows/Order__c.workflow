<?xml version="1.0" encoding="UTF-8"?>
<Workflow xmlns="http://soap.sforce.com/2006/04/metadata">
    <alerts>
        <fullName>Confirm</fullName>
        <description>Confirm</description>
        <protected>false</protected>
        <recipients>
            <field>cst_email__c</field>
            <type>email</type>
        </recipients>
        <senderType>CurrentUser</senderType>
        <template>unfiled$public/Confirmation</template>
    </alerts>
</Workflow>
